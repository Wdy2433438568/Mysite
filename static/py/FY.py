class Pageinfo:
    def __init__(self,current_page,all_count,per_page,base_url,show_page=11):
        """
        :param current_page:当前页
        :param all_count:总行数
        :param per_page:每页显示行数
        :param show_page:显示多少页
        """
        self.base_url = base_url
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        a,b = divmod(all_count,per_page)
        if b:
            a = a + 1
        self.all_page = a
        self.show_page = show_page
    def page(self):
        page_list = []
        half = int((self.show_page-1) / 2)

        #如果数据总页数<11
        if self.all_page< self.show_page:
            begin = 1
            stop = self.all_page + 1
        else:
            #如果当前页<=5 则永远显示1-11页
            if self.current_page <= half:
                begin = 1
                stop = self.show_page + 1
            else:
                if self.current_page + half > self.all_page:
                    stop = self.all_page + 1
                    begin = self.all_page - 10
                else:
                    begin = self.current_page - half
                    stop = self.current_page + half +1
        if self.current_page <= 1:
            page_list.append('<a href="#">上一页</a>')
        else:
            page_list.append('<a href="%s?page=%s">上一页</a>'%(self.base_url,self.current_page - 1))
        # begin = self.current_page - half
        # stop = self.current_page + half + 1
        for i in range(begin,stop):
            if i == self.current_page:
                temp = "<a  href='%s?page=%s'>%s</a>"%(self.base_url,i,i,)
            else:
                temp = "<a  href='%s?page=%s'>%s</a>"%(self.base_url,i,i,)

            page_list.append(temp)
        if self.current_page >= self.all_page:
            page_list.append('<a href="#">下一页</a>')
        else:
            page_list.append('<a href = "%s?page=%s">下一页</a>'% (self.base_url,self.current_page + 1))

        return ''.join(page_list)

    def start(self):
        return (self.current_page - 1) * self.per_page
    def end(self):
        return self.current_page * self.per_page