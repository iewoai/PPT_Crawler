# PPT_Crawler
scrapy的使用（爬取第一PPT网上所有的ppt，并规范化储存）

一、程序说明

    1.ppt/spiders/ppt1.py为主程序，爬取所有ppt信息

    2.ppt/spiders/normalize.py为规范化脚本，包括解压所有的ppt压缩文件（ppt是以压缩包的形式下载的），删除解压出来的垃圾文件（包括.html，.url和.link文件）