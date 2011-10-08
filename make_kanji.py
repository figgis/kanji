#!/usr/bin/env python

"""
Download kanji from
http://www.csus.edu/indiv/s/sheaa/projects/genki/kanji_main.html

for i in {3..12}; do wget http://aitweb.csus.edu/fl/japn/genki_kanji_table.php?lesson=$i; done

for i in {1..145}; do wget http://aitweb.csus.edu/fl/japn/genki_kanji_examples.php?id=$i; done
"""
import urllib2
from BeautifulSoup import BeautifulSoup
import sys
import codecs
import os
from latex_template import *

#Helper function
def printheader(word):
    '''generate a nice header string'''
    out.write("\n%s\n%s\n" % (word, '-' * len(word)))

out = codecs.getwriter('utf-8')(sys.stdout)

class Character:
#    def __init__(self, kanji, reading, definition,example_url,lesson):
    def __init__(self, character):
        # dictionary
        self.character=character
        self.example=[]

    def add_example(self, example_list):
        """pass
        """
        for i in example_list:
            self.example.append(i)

    def show(self):
        """pass
        """
        out.write("kanji:%s\n" % self.character['kanji'])
        out.write("reading:%s\n" % self.character['reading'])
        out.write("definition:%s\n" % self.character['definition'])
        out.write("example_url:%s\n" % self.character['example_url'])
        out.write("lesson:%s\n" % self.character['lesson'])
        print 'Example:'
        for i in self.example:
            i.__show()
        print

    def __show(self):
        out.write("kanji:%s\n" % self.character['kanji'])
        out.write("reading:%s\n" % self.character['reading'])
        out.write("definition:%s\n" % self.character['definition'])

    def latex(self):
        """pass
        """
        ex=''
        for n,i in enumerate(self.example):
            if n > 12:
                break
            ex+=r'\\'
            ex+=i.character['kanji']+';'
            ex+=i.character['reading']+';'
            ex+=i.character['definition']
        self.character['example']=ex
        s=card_template.safe_substitute(self.character)
        out.write(s)

class Lesson:
    def __init__(self,url):
        self.root='http://aitweb.csus.edu/fl/japn/'
        self.url=url
        self.words=[]
        self.__examples=[]
        self.lesson=url.split('=')[1]
        self.__example_url=None

        self.words=self.__parse(url)
        for i in self.words:
            i.add_example(self.__parse(i.character['example_url']))

    def show(self):
        for i in self.words:
            i.show()

    def latex(self):
        for i in self.words:
            i.latex()

    def __insert(self,kanji_list):
        """pass
        """
        for i in kanji_list:
            self.words.append(Character(i[0][0],i[0][1],i[0][2],i[0][3]))
            self.words[-1].add_example(i[1])

    def __parse(self,url,kind=None):
        """pass
        """
        path=os.path.join('genki',url)
        ### tmp solution
        #page=urllib2.urlopen(src+url)
        with open(path) as fd:
            page=fd.read()
        ###
        soup=BeautifulSoup(page)
        ###
        table = soup.find("table")
        rows = table.findAll('tr')

        character_list=[]
        c={}

        for r in rows[1:]:
            c={}
            cols=r.findAll('td')
            c['kanji']=cols[0].text
            c['reading']=cols[1].text
            c['definition']=cols[2].text
            c['lesson']=self.lesson
            try:
                go=cols[3].findAll('a')[0]['href'].split(',')[0].split("'")[1]
            except IndexError:
                go=None
            c['example_url']=go
            character_list.append(Character(c))
        return character_list

my_kanji=[]
for i in range(3,13):
#for i in range(3,4):
    src='genki_kanji_table.php?lesson='+str(i)
    my_kanji.append(Lesson(src))

out.write(latex_pre)
for i in my_kanji:
    i.latex()
#   i.show()
out.write(latex_post)


# vim: set fileencoding=utf-8 expandtab:
