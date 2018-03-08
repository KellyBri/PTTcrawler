from pyquery import PyQuery as pq

#get all the 'r-ent' block of woman board of PTT
def get_html():

	#get html code of woman board of PTT
	source = pq(url='https://www.ptt.cc/bbs/WomenTalk/index.html')
	item = source('.r-ent')

	for i in range(3):

		for a in source.items('a'):

			btn = a('.btn')
			if btn.text() == '‹ 上頁':
				#get the relative path of the previous page
				source = pq( url='https://www.ptt.cc/' + btn.attr('href') )	
				item += source('.r-ent')

	return item


def crawler(source):

	word = ''

	for item in source.items():

		title = item('.title').text()				#get the text of the 'title' class

		#there doesn't exist '本文已被刪除' and '版規' in title
		if title.find('本文已被刪除') == -1 and title.find('公告') == -1 :
			
			print(title)
			
			url_article = item('a').attr('href')	#get the relative path of the article
			src = pq( url = 'https://www.ptt.cc/' + item('a').attr('href') )
			src('.article-metaline').remove()		#remove article-metaline class 		(標題、作者、時間)
			src('.article-metaline-right').remove()	#remove article-metaline-right class(看板)
			src('.f2').remove()						#remove f2 class 	(發信站、網址)
			src('.push').remove()					#remove push class 	(回覆)

			print(src('#main-content').text())
			

if __name__ == '__main__':

	crawler( get_html() )


	
