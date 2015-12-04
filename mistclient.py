# from test_model import *s
import json
import os
import requests
import yaml
from dateutil.parser import parse as dateparser
# swaggerjs = yaml.load(open("mist-api.yaml").read())
# model = yaml.load(open("client-model.yaml").read())
import responses
import inspect

class Swagger(object):

    def __init__(self, swagger):
        self.basePath = swagger["basePath"]
        self.host = swagger["host"]
        self.uri = swagger["host"] + swagger["basePath"]
        self.scheme = swagger.get("schemes", ["http"])[0]
        self.securityHeaders = []
        self.paths = paths = swagger["paths"]
        self.definitions = swagger.get("definitions", {})
        if swagger.get("securityDefinitions"):
            for sec in swagger["securityDefinitions"]:
                if swagger["securityDefinitions"][sec]["type"] == "apiKey":
                    if swagger["securityDefinitions"][sec]["in"] == "header":
                        name = swagger["securityDefinitions"][sec]["name"]
                        self.securityHeaders.append(name)
        for path in paths:
            for method in paths[path]:
                opid = paths[path][method]["operationId"]
                setattr(self, opid, ApiRequest(path, method, paths[path][
                        method], self.definitions, self.securityHeaders))


class ApiRequest(object):

    def __init__(self, path, method, data, definitions, default_params=None,
                 security=None):
        if default_params is None:
            default_params = {}
        if security is None:
            security = {}

        self.path = path
        self.method = method
        self.data = data
        self.header_params = []
        self.path_params = []
        self.body_params = []
        self.required_params = []
        self.parameters = []
        self.default_params = default_params
        self.id = data["operationId"]
        if data.get("parameters"):
            for param in data["parameters"]:
                name = param["name"]
                place = param["in"]
                if place == "header":
                    self.parameters.append(name)
                    if param.get("required"):
                        self.required_params.append(name)
                    self.header_params.append(name)
                if place == "path":
                    self.parameters.append(name)
                    self.required_params.append(name)
                    self.path_params.append(name)
                if place == "body":
                    if param["schema"].get("$ref"):
                        body_params = definitions[
                            param["schema"]["$ref"].split("/")[2]]
                    else:
                        body_params = param["schema"]
                    properties = body_params["properties"]
                    required = body_params.get("required", [])
                    for p in body_params["properties"]:
                        self.parameters.append(name)
                        if p in required:
                            self.required_params.append(p)
                        self.body_params.append(p)
        if data.get("security") == {}:
            pass
        else:
            self.parameters.append(security)
            self.required_params.extend(security)

    def __call__(self, *args, **kwargs):
        for p in self.required_params:
            if not kwargs.get(p):
                raise Exception("Parameter {0} missing".format(p))
        print self.method, self.path.format(*args, **kwargs), self.id, kwargs
        try:
            return getattr(responses, self.id)
        except:
            return {"error": "not_implemented"}


class Helpers(object):

    def _get_config(self,):
        pass

    def _type(self, param_name, param_type, **kwargs):
        types = {
            str: "string",
            int: "integer",
            bool: "boolean"
        }
        param = kwargs.get(param_name)
        if param:
            if types[type(param)] == param_type:
                return kwargs
            else:
                problem = "Parameter {0} should be of type {1}".format(
                    param_name,
                    param_type)
                raise Exception(problem)
        return kwargs

    def _ref(self, param_name, input_name, **kwargs):
        input_value = kwargs.get(input_name)
        if input_value:
            kwargs[param_name] = input_value
            kwargs.pop(input_name)
            return kwargs
        return kwargs

    def _default(self, param_name, default_value, **kwargs):
        input_value = kwargs.get(param_name)
        if not input_value:
            kwargs[param_name] = default_value
            return kwargs
        return kwargs

    def _exists(self, param_name, exists, **kwargs):
        param = kwargs.get(param_name, False)
        if exists and param:
            return True
        if not exists and not param:
            return True
        return False

    def _set(self, input_name, property_name, **kwargs):
        # print"set ",input_name,property_name
        if kwargs.get("$response"):
            kwargs = kwargs["$response"]
        if input_name == "$body":
            setattr(self, property_name, kwargs)
        else:
            setattr(self, property_name, kwargs.get(input_name))
        return True

    def _in(self, param_name, enum, **kwargs):
        param = kwargs.get(param_name)
        if param and param in enum:
            return True
        return False

    def _eq(self, param_name, value, **kwargs):
        param = kwargs.get(param_name)
        if param and param == value:
            return True
        return False
    def _required(self,param_name,value,**kwargs):
        if kwargs.get(param_name):
            return kwargs
        problem = "Parameter {0} is required".format(param_name)
        raise Exception(problem)

    def _get_valid_case(self, cases, **kwargs):
        for case in cases:
            if self._check_case(case["case"], **kwargs):
                return case
        valid_cases = json.dumps(cases, sort_keys=True, indent=4, separators=(',', ': '))
        problem = "Every `case` in `init` was found invalid."
        problem += "Valid cases are: {0}".format(valid_cases)
        raise Exception(problem)

    def _init(self, case, **kwargs):
        # print"initing case",case
        action = case.get("action", None)
        # printaction
        response_schema = case.get("response", {})
        if type(action) == str:
            funcact = getattr(self._spec, action)
            # printfuncact.parameters
            response = funcact(**kwargs)
            for param_name in response_schema:
                schema = response_schema[param_name]
                if type(response) == list:
                    response = {"$response": response}
                for action in schema:
                    if not self._run(action, param_name, schema[action], **response):
                        problem = "Action {0} with parameters {1},{2} failed to\
                                   execute!".format(action, param_name,
                                                    schema[action])
                        raise Exception(problem)
            return True
        elif type(action) == list:
            pass
        elif type(action) == dict:
            pass
        else:
            return True
            # problem = "Every `case` in `init` property must? have an action"
            # raise Exception(problem)

    def _call_api(self, api_call, **kwargs):
        pass

    def _call_api_set(param_name, api_call, **kwargs):
        pass

    def _set_from_config(self, property_name, config_key, **kwargs):
        if self._config.get(config_key):
            setattr(self, property_name, self._config[config_key])
            return True
        return False

    def _filter(self, keys, response, **kwargs):
        for key in keys:
            query = kwargs.get(key)
            if query:
                return [item for item in response if item.get(key) == query]
        return response

    def _search(self, _search_query, _response, **kwargs):
        
        value = kwargs.get(_search_query)
        if not value:
            return _response
        answer = []
        for item in _response:
            if type(item) == str:
                item = _response[item]
            stritem = json.dumps(item)
            if value in stritem:
                answer.append(item)
        return answer
    def _items(self,items,response, **kwargs):
        answer = []
        for action in items:
            for item in response:
                item = self._run(action, items[action], item, **kwargs)
                answer.append(item)
        return answer
    def _entity(self, item, data, **kwargs):
        print data , kwargs
        ent = getattr(self, "__"+item)
        print ent._attributes
        for attr in ent._attributes:
            if not data.get(attr):
                if hasattr(self,attr):
                    data[attr] = getattr(self,attr)
                elif kwargs.get(attr):
                    data[attr]=kwargs[attr]

        return getattr(self, "__"+item)(**data)

    def _check_case(self, case, **kwargs):
        case = case.get('$if')

        if case:
            # print"checking case..", case
            for param in case:
                for check in case[param]:
                    valid = self._run(check, param, case[
                                      param][check], **kwargs)
                    if not valid:
                        # print"not valid", check, param, case[param][check]
                        return False
            return True
        else:
            return True

    def _run(self, helper, parent, value, **kwargs):
        if helper.startswith("$"):
            return getattr(self, helper.replace("$", "_"))(parent, value, **kwargs)


class Client(object):

    def __init__(self, url, basePath="api", modelName="model"):
        modelurl = "{0}/{1}/{2}.yaml".format(url, basePath, modelName)
        response = requests.get(modelurl)
        self.model = yaml.load(response.content)
        self.root = self.model.get("root")
        api_spec = self.model.get("api-spec")
        specurl = "{0}/{1}/{2}.yaml".format(url, basePath, api_spec)
        response = requests.get(specurl)
        self.spec = Swagger(yaml.load(response.content))
        if self.model.get("config_path"):
            home_path = os.getenv("HOME")
            save_path = self.model["config_path"]
            self.__config_path = os.path.join(home_path, "." + save_path)
            if os.path.isfile(self.__config_path):
                with open(self.__config_path) as f:
                    self.__config = yaml.load(f.read())
            else:
                self.__config = {}
                self.__config_path = ""
        else:
            self.__config = {}
            self.__config_path = ""

    def __call__(self, entity=None):
        # print"creating entity:",entity
        if entity == None:
            entity = self.root
            Entity = self.model["entities"][entity]
        else:
            Entity = self.model["entities"][entity]
        parameters = Entity.get("parameters", {})
        init_cases = Entity.get("init")
        properties = Entity.get("_properties")
        attributes = Entity.get("attributes",[])
        prepare_steps = Entity.get("prepare")
        action = Entity.get("action")
        methods = Entity.get("methods", {})
        response = Entity.get("response")
        cls = type(entity, (Helpers, object), {})
        config = self.__config
        config_path = self.__config_path
        spec = self.spec
        setattr(cls, "_parameters",parameters)
        setattr(cls, "_attributes",attributes)
        setattr(cls, "_config",config)
        setattr(cls, "_config_path",config_path)
        setattr(cls, "_spec", spec)
        setattr(cls, "_init_cases",init_cases)
        setattr(cls, "_prepare_steps",prepare_steps)
        def init(self, entity=Entity, **kwargs):
            # printkwargs
            parameters = self._parameters
            for param_name in parameters:
                for action in parameters[param_name]:
                    value = parameters[param_name][action]
                    # printkwargs, action, param_name, value
                    kwargs = self._run(action, param_name, value, **kwargs)
            for p in attributes:
                value = kwargs.get(p)
                if value:
                    setattr(self,p,value)
            if self._init_cases:
                # print"getting cases"
                case = self._get_valid_case(init_cases, **kwargs)
                self._init(case["case"], **kwargs)
            if self._prepare_steps:
                for step in self._prepare_steps:
                    if self._check_case(step["step"]):
                        self._init(step["step"], **kwargs)

        setattr(cls, "__init__", init)
        if properties:
            setattr(cls, "_properties",properties)
            def _getattr_(self, name):
                try:
                    return object.__getattribute__(self, name)
                except:
                    if self._properties.get(name):
                        self._init(self._properties[name])
                        del self._properties[name]
                    return object.__getattribute__(self, name)

            setattr(cls, "__getattribute__", _getattr_)
        for method_name in methods:
            method = methods[method_name]

            def decorated_method(self, method=method, name=method_name, *args, **kwargs):
                action = method.get("action")
                parameters = method.get("parameters", {})
                switch_cases = method.get("switch")
                response_schema = method.get("response", {})
                for attr in self._attributes:
                    kwargs[attr] = getattr(self,attr)
                for param_name in parameters:
                    for act in parameters[param_name]:
                        value = parameters[param_name][act]
                        kwargs = self._run(act, param_name, value, **kwargs)
                if switch_cases:
                    case = self._get_valid_case(switch_cases, **kwargs)
                    if case.get("action"):
                        self._init(case, **kwargs)
                funcact = getattr(self._spec, action)
                
                response = funcact(**kwargs)
                for act in action_order:
                    if act in response_schema:
                        print act,response_schema[act]
                        response = self._run(act,response_schema[act],response ,**kwargs)
                        
                for act in response_schema:
                    if not act.startswith("$"):
                        for act2 in response_schema[act]:
                            self.run(act2,act,response[act][act2],**response)
                return response            
            decorated_method.__name__ = method_name
            decorated_method.func_name = method_name
            setattr(cls, method_name, decorated_method)
        if not entity == self.root:
            return cls
        for ent in self.model["entities"]:
            if ent != self.root:
                entcls = Client.__call__(self, ent)
                setattr(cls, "__" + ent, entcls)
        return cls

action_order = ["$filter","$search","$items"]


newcls = Client("http://localhost:8000")
MistClient = newcls()
