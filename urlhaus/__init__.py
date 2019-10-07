#=======================================================
# Simple python class for querying urlhaus's api.
#=======================================================
import requests
import json
import re

__version__ = '0.0.2'

class UrlHaus:
    """ A simple class to query the urlhaus public api."""

    def __init__(self, api_key=None):
        self.__bulk_api_url = "https://urlhaus-api.abuse.ch/v1/"
        self.__submission_url = "https://urlhaus.abuse.ch/api/"
        self._api_key = api_key


    @property
    def api_url(self):
        return self.__api_url


    """
        borrowed from https://github.com/cocaman/urlhaus/blob/master/urlhaus.py
        helper function to check that a tag has the right format [A-Za-z0-9.-]
    """
    def check_tag_regex(s):
        if s == "":
            return 
        p = re.compile(r'([a-zA-Z\.-]+)')
        m = p.match(s)
        if m == None or not m.group() == s:
            raise Exception("Invalid tag used '" + s + "'")
        return str(s)

    def submit_url(self, url, threat="malware_download", tags=[]):
        for tag in tags:
            check_tag_regex(tag)

        if not url:
            raise Exception("no url passed to submission")

        if not self._api_key:
            raise Exception("no api key provided")

        json_data = {
            'token' : api_key,
            'submission' : [
                {
                    'url' : url,
                    'threat' : threat,
                    'tags' : tags
                }
             ]
        }
        try:
            r = requests.post(self.__submission_url, json=json_data, timeout=15, headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)} )
        except Exception as e:
            raise Exception("Unable to post url to api. Recieved the following error {}".format(e))


    def pull_recent_urls(self):
        try:
            r = requests.get("{}urls/recent/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def pull_recent_payloads(self):
        try:
            r = requests.get("{}payloads/recent/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_url(self,url):
        try:
            r = requests.post("{}url/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"url": url})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_urlid(self,urlid):
        try:
            r = requests.post("{}urlid/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"urlid": urlid})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))


    def lookup_by_host(self,host):
        try:
            r = requests.post("{}host/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"host": host})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_hash(self,hash):
        hash_type = "unknown"
        if len(hash) == 32:
            hash_type = "md5_hash"
        elif len(hash) == 64:
            hash_type = "sha256_hash"
        else:
            raise Exception("invalid hash type provided in lookup")

        try:
            r = requests.post("{}payload/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={hash_type: hash})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")


        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_tag(self,tag):
        try:
            r = requests.post("{}tag/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"tag": tag})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_signature(self,signature):
        try:
            r = requests.post("{}signature/".format(self.__bulk_api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"signature": signature })
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def download_sample(self,sha256):
        if not len(sha256) == 64:
            raise Exception("invalid sha256")

        try:
            r = requests.get("{}download/{}".format(self.__bulk_api_url, sha256), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.content
            else:
                raise Exception("Unable to read response")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))
