"""
This module contains functions for MLW library which will help download & upload resources from JEG to MLW.
"""

import requests
import json
from mlwlib.base.constants import URLS, BYPASS_PROXY
from mlwlib.base.base import HTTPClient


class MLWClient():
    """
    MLWClient class, contains methods for project operations like resource download, resource upload etc.

    """
    def __init__(self, c8y_base_url):
        """
        init method of Project class
        
        :param c8y_base_url: base url of cumulosity mlw tenant
        :type c8y_base_url: String
        """
        self.__c8y_base_url = c8y_base_url
        self.__client = HTTPClient(c8y_base_url)
        self.__request_session = self.__client.request_session

    def list_projects(self):
        """
        List all projects in a MLW Tenant.

        :return: dictionary of projects
        :type: dictionary
        """
        try:  
            dict_of_projects = {}
            project_url = URLS.MLW.PROJECTS.format(self.__c8y_base_url)
            response = self.__request_session.get(project_url)
            if response.status_code == 200:
                project_data=json.loads(response.text)['data']
                if project_data:
                    for project in project_data:
                        dict_of_projects[project["id"]]= {"name": project["name"]}
                return dict_of_projects
            else:
                raise requests.HTTPError("Unable to fetch projects from MLW")
        except Exception as ex:
            return {
                "projectList": None,
                "message":"Unable to fetch projects from MLW",
                "exception": ex
            }
    
    def project(self, project_id):
        """
        Create Project class object for a given project_id.

        :param project_id: Id of target project
        :type project_id: String

        :return: Project class object
        :type: class object
        """
        return Project(self.__client, project_id)


class Project():
    """
    Project class, contains methods for project operations like list resource in a project, resource upload to a project etc.

    """
    def __init__(self, client, project_id):
        """ 
        init method of Project class
        
        :param project_id: Id of target project
        :type project_id: String
        """
        self.__client = client 
        self.__c8y_base_url = self.__client.c8y_base_url
        self.__request_session = self.__client.request_session
        self.__project_id = project_id

    def list_resources(self):
        """
        list_resources method in Project class. List all resources in a MLW project.

        :return: list of resources in a MLW project
        :type: dictionary
        """
        try:
            list_of_resources = {}
            resources_url = URLS.MLW.RESOURCES.format(self.__c8y_base_url, self.__project_id)
            response = self.__request_session.get(resources_url)
            if response.status_code == 200:
                resource_data=json.loads(response.text)
                if resource_data:
                    list_of_resources["project_id"] = resource_data["id"]
                    list_of_resources["project_name"] = resource_data["name"]
                    list_of_resources["resources"] = resource_data["resources"]
                return {"resourceList": list_of_resources}
            else:
                raise requests.HTTPError("Unable to fetch list of resources from MLW")
        except Exception as ex:
            return {
                "resourceList": None,
                "message": "Unable to fetch list of resources for project "+ self.__project_id + " from MLW",
                "exception": ex
            }

    def upload_resource(self, resource_path):
        """
        upload_resource method in Project class. Upload a resource to a project in MLW.

        :param resource_path: path of the resource which needs to be uploaded
        :type resource_path: String

        :return: dictionary with message
        :type: dictionary
        """
        try:
            upload_url = URLS.MLW.UPLOAD_RESOURCE.format(self.__c8y_base_url, self.__project_id)
            files = {'file': open(resource_path,'rb')}
            response = self.__request_session.post(upload_url, proxies=BYPASS_PROXY, files=files)
            if response.status_code == 200:
                return {"msg": "Resource uploaded to MLW successfully."}
            else:
                raise requests.HTTPError("Resource upload to MLW failed.")
        except Exception as ex:
            return {
                "message": "Resource upload to MLW failed.",
                "exception": ex
            }

    def resource(self, resource_name):
        """
        resource method in Project class. Create Resource class object for a given resource name.

        :param resource_name: name of resource
        :type project_id: String

        :return: Resource class object
        :type: class object
        """
        return Resource(self.__client, self.__project_id, resource_name)


class Resource():
    """
    Resource class, contains methods for resource operations like resource download etc.

    """
    def __init__(self, client, project_id, resource_name):
        self.__client = client
        self.__c8y_base_url = self.__client.c8y_base_url
        self.__request_session = self.__client.request_session
        self.__project_id = project_id
        self.__resource_name = resource_name

    def download_resource(self):
        """
        download_resource method in Resource class. Download a resource from a project in MLW.

        :return: dictionary with message
        :type: dictionary
        """
        try:
            download_url = URLS.MLW.DOWNLOAD_RESOURCE.format(self.__c8y_base_url, self.__project_id, self.__resource_name)
            response = self.__request_session.get(download_url, proxies=BYPASS_PROXY)
            if response.status_code == 200:
                open(self.__resource_name, 'wb').write(response.content)
                return {"msg": "Resource downloaded from MLW successfully."}
            else:
                raise requests.HTTPError("Resource download failed from MLW.")
        except Exception as ex:
            return {
                "message": "Resource, " + self.__resource_name + " download failed from MLW.",
                "exception": ex
            }


