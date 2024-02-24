from typing import Text,Dict


from langchain.schema.language_model import BaseLanguageModel
from langchain.schema.agent import AgentAction
from langchain_core.agents import AgentAction
from langchain.agents import AgentExecutor, MRKLChain
from langchain.agents.agent_toolkits.openapi.toolkit import OpenAPIToolkit
from langchain.agents.agent_toolkits.openapi.spec import ReducedOpenAPISpec,reduce_openapi_spec
from langchain.agents.agent_toolkits.openapi.planner import create_openapi_agent
from langchain.agents.agent_toolkits.openapi.planner_prompt import API_ORCHESTRATOR_PROMPT, API_PLANNER_PROMPT,API_CONTROLLER_PROMPT
from langchain.agents.mrkl.base import ZeroShotAgent
from langchain.requests import RequestsWrapper


class APIAgent():
    def __init__(self,
                 llm : BaseLanguageModel, 
                 openapi_doc_path :Text= None,
                 openapi_spec: ReducedOpenAPISpec = None, 
                 ) -> None:
        self.llm  = llm
        self.openapi_doc_path = openapi_doc_path
        self.openapi_spec = openapi_spec
        self.openapi_agent =  self._build_openapi_agent()
        self.requsts_wrapper = self._build_requests_wrapper()


    def run(self, query:Text):
        """
        1 . query -> planer -> plan
        2.  plan -> controller -> tool
        3.  plan -> tool -> request

        """
        output = self.openapi_agent.run(query)
        return output
    
    

    def _build_openapi_agent(self) ->AgentExecutor :
        openapi_agent = create_openapi_agent(api_spec=self.openapi_spec,requests_wrapper=self.requsts_wrapper,
                                             llm= self.llm)
        return openapi_agent
    
    def _build_requests_wrapper(self)-> RequestsWrapper:
        pass

