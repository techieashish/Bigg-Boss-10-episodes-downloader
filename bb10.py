__author__ = 'ASHISH'
import  requests, bs4, time , re, sys


class BB():
    pages = ["http://moviestab.com/15-category/bigg-boss-10.html"]
    episodes_list = []
    episodes_name = []

    def __init__(self):
        self.page()

    def extract(self, url, css=None):
        self.url = url
        while True:
            try:
                global res
                res = requests.get(url, stream=True)
            except (Exception, requests.RequestException , ConnectionError, TimeoutError):
                sys.stdout.write("\n\n          Connection Error Occurred.. Retrying in 10 seconds")
                time.sleep(10)
                continue
            else:
                break
        if css == 'res1':
            return res
        else:
            soup  = bs4.BeautifulSoup(res.text, 'html.parser')
            data = soup.select(css)
            return data

    def page(self):
         css = "div.pagination.pull-right > a[href]"
         all_pages = self.extract(self.pages[0],css)
         for i in range(len(all_pages)-1):
             self.pages.append(all_pages[i].get('href'))
         self.episodes()

    def episodes(self):
        for i in range(len(self.pages)-1):
            url = self.pages[i]
            css = "div.listed > a[href]"
            epi_data = self.extract(url, css)
            for e in epi_data:
                self.episodes_list.append(e.get('href'))
            css1 = "div.details > a > h3"
            name_data = self.extract(url,css1)
            for names in name_data:
                self.episodes_name.append(names.text)
        self.display()

    def display(self):
        counter = 1
        for names in self.episodes_name:
            print("\n%d." % counter+names)
            counter +=1


    def down(self, arg, arg1,arg2):
        sys.stdout.write("\nGrabbing Video")
        self.arg = arg
        self.arg1 = arg1
        self.arg2 = arg2
        dl = 0
        post_percent = 0
        url = self.episodes_list[self.arg]
        css = "a"
        parse = self.extract(url, css)
        if self.arg1 == 1:
            info = parse[6].get('href')
        else:
            info = parse[5].get('href')
        res = self.extract(info, "res1")
        file_size = int(res.headers.get('content-length'))
        print('\n\nSize: %.2f MB' %(float(file_size/(1024*1024))))
        path = self.arg2
        file = open('%s\%s.mp4' % (path, self.episodes_name[self.arg]), 'wb')
        sys.stdout.write("\n")
        for chunk in res.iter_content(chunk_size=1024):
            file.write(chunk)
            dl += len(chunk)
            percent = int((dl/file_size) * 100)
            if (percent%2) == 0 and (percent > post_percent):
                sys.stdout.write("\r%s Downloaded : %s%%"% (self.episodes_name[self.arg], percent))
                sys.stdout.flush()
                post_percent = percent
        sys.stdout.write("\n\nCompleted\n")







