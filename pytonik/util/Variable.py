# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 3/4/20.
import os
from pytonik import Version


class Variable:

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def put(self, path="", host="", port="", para="", status=200, accept="", method="GET", cookies="", ssl_v="off", referral=""):
        uri, query_string = "", ""  # path.split('/')[-1]+str(para)
        host = str(host) if str(
            host) != "" else os.environ.get("HTTP_HOST", "")
        port = str(port) if str(
            port) != "" else os.environ.get("SERVER_PORT", "")
        path = str(path) if str(
            path) != "" else os.environ.get("PATH_INFO", "")
        status = str(status) if status != "" else os.environ.get(
            "REDIRECT_STATUS", "")

        cookies = str(cookies) if str(
            cookies) != "" else os.environ.get("HTTP_COOKIE", "")

        referral = str(referral) if str(
            referral) != "" else os.environ.get("HTTP_REFERER", "")
      
        if para.find("?") == True:
            parts = para.split('?')
            if len(parts) > 1:
                uri = parts[0]
                query_string = parts[1]
            else:
                uri = ""
                query_string = parts[0]

        else:
            query_string = ""
            uri = ""

        env = {
            "Framework": Version.AUTHOR if Version.AUTHOR != "" else os.environ.get("Framework", ""),
            "X-Version": Version.VERSION_TEXT if Version.VERSION_TEXT != "" else os.environ.get("X-Version", ""),
            "X-Organisation": Version.ORG if Version.ORG != "" else os.environ.get("X-Organisation", ""),
            "PATH_INFO": para,
            "HTTP_HOST": host,
            "SERVER_PORT": port,
            "HTTP_COOKIE": cookies,
            "REDIRECT_STATUS": status,
            "HTTP_ACCEPT": str(accept) if accept != "" else os.environ.get("HTTP_ACCEPT", ""),
            "DOCUMENT_ROOT": path,
            "REQUEST_METHOD": str(method) if method != "" else os.environ.get("REQUEST_METHOD", ""),
            "QUERY_STRING": str(query_string),
            'SERVER_SOFTWARE': Version.AUTHOR if Version.AUTHOR != "" else os.environ.get("SERVER_SOFTWARE", ""),
            'PATH_TRANSLATED': str(path) + "/public",
            'HTTPS': ssl_v,
            'HTTP_REFERER': referral,
            "REQUEST_URI": "/"+str(os.path.basename(os.getcwd()))+str(para)
        }
        
        if Version.PYVERSION_MA <= 2:
            lt = env.iteritems()
        else:
            lt = env.items()
        if os.environ.get("REQUEST_URI", "") != "" or os.environ.get("REQUEST_URI", "") != None:
            os.environ.clear()
            os.environ.update(dict(env))

        for k, v in lt:
            os.environ.setdefault(str(k), str(v).encode())

        os.environ.update(dict(REQUEST_URI=os.environ.get("REQUEST_URI")))

    def out(self, key, alt=""):
        return os.environ.get(key, alt)

    def see(self):
        return os.environ
