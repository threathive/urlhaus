#=======================================================
# Simple python class for querying urlhaus's api.
#=======================================================
import requests

__version__ = '0.0.1'

class UrlHaus:
    """ A simple class to query the urlhaus public api."""

    def __init__(self):
        self.__api_url = "https://urlhaus-api.abuse.ch/v1/"

    @property
    def api_url(self):
        return self.__api_url

    def pull_recent_urls(self):
        try:
            r = requests.get("{}urls/recent/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def pull_recent_payloads(self):
        try:
            r = requests.get("{}payloads/recent/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_url(self,url):
        try:
            r = requests.post("{}url/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"url": url})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_urlid(self,urlid):
        try:
            r = requests.post("{}urlid/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"urlid": urlid})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))


    def lookup_by_host(self,host):
        try:
            r = requests.post("{}host/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"host": host})
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
            r = requests.post("{}payload/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={hash_type: hash})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")


        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_tag(self,tag):
        try:
            r = requests.post("{}tag/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"tag": tag})
            if r.ok:
                return r.json()
            else:
                raise Exception("Unable to read response as json")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))

    def lookup_by_signature(self,signature):
        try:
            r = requests.post("{}signature/".format(self.__api_url), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)}, data={"signature": signature })
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
            r = requests.get("{}download/{}".format(self.__api_url, sha256), headers={"User-Agent" : "urlhaus-python-client-{}".format(__version__)})
            if r.ok:
                return r.content
            else:
                raise Exception("Unable to read response")

        except Exception as e:
            raise Exception("Unable to connect to api. Recieved the following error {}".format(e))
