import requests
import sys
import colorama

class scan:

    def __init__(self,site):
        self.site = site
        self.lists = open("list.txt","r").readlines()

    def find(self):
        for _ in self.lists:
            _ = _.split("\n")
            self.now_site = _[0]+"."+self.site
            try:
                self.req = requests.get(
                    "https://"+self.now_site
                    )
            except:
                pass

            if self.req.status_code  == 200:
                print (f"\033[92m[200]\033[97m {self.now_site}")

        return "finish"

if __name__=="__main__":
    start = scan(sys.argv[1])
    start.find()