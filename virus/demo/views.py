from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./demo/templates"))

from pyecharts import options as opts
from pyecharts.charts import Tab
from demo.AllInOneHtml import pneumonia

def index(request):
    targetProvinceName = 0
    additionProvinceName = {"四川"}
    gotProvinceName = {"四川"}
    additionMapName = {"四川"}
    v=pneumonia(targetProvinceName, additionProvinceName, gotProvinceName, additionMapName)
    tab=Tab("疫情地图豪华定制版")
    tab.add(v.getSichuanMap("currentConfirmedCount","现存确诊"),"四川现存")
    tab.add(v.getSichuanMap("confirmedCount","累计确诊"),"四川累计")
    tab.add(v.getSichuanTable(),"四川表格")
    tab.add(v.getChinaMap("currentConfirmedCount","现存确诊"),"中国现存")
    tab.add(v.getChinaMap("confirmedCount","累计确诊"),"中国累计")
    tab.add(v.getProvinceTable(),"各省表格")
    tab.add(v.getWorldMap("currentConfirmedCount","现存确诊"),"世界现存")
    tab.add(v.getWorldMap("confirmedCount","累计确诊"),"世界累计")
    tab.add(v.getWorldTable(),"世界表格")
    return HttpResponse(tab.render_embed())