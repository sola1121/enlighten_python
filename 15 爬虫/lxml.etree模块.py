# XPath语言: 可以用来提取xml, HTML信息的语言
# 在python中使用lxml模块用于解析XML文档树

from lxml import etree

xml_str = \
"""<?xml version="1.0" encoding="utf-8"?>
<CATALOG>
	<PLANT>
		<COMMON>Bloodroot</COMMON>
		<BOTANICAL>Sanguinaria canadensis</BOTANICAL>
		<ZONE>4</ZONE>
		<LIGHT desc="sure">Mostly Shady</LIGHT>
		<PRICE>$2.44</PRICE>
		<AVAILABILITY>031599</AVAILABILITY>
	</PLANT>
	<PLANT>
		<COMMON>Columbine</COMMON>
		<BOTANICAL>Aquilegia canadensis</BOTANICAL>
		<ZONE>3</ZONE>
		<LIGHT desc="not sure">Mostly Shady</LIGHT>
		<PRICE>$9.37</PRICE>
		<AVAILABILITY>030699</AVAILABILITY>
	</PLANT>
	<PLANT>
		<COMMON>Cowslip</COMMON>
		<BOTANICAL>Caltha palustris</BOTANICAL>
		<ZONE>4</ZONE>
		<LIGHT desc="sure">Mostly Shady</LIGHT>
		<PRICE>$9.90</PRICE>
		<AVAILABILITY>030699</AVAILABILITY>
	</PLANT>
</CATALOG>
"""

# 根节点
root = etree.fromstring(bytes(xml_str, encoding="utf-8"))
# print(root)

element = root.xpath("//PLANT/COMMON")
print(element[0].text)
print(element[1].text)

attribute = root.xpath("//@desc")
print(attribute)
