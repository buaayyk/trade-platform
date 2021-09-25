from django.shortcuts import HttpResponse,render,redirect


def own(request):
    return render(request, 'own.html',{"Tittle":'小仙女',"sTittle":"快点好起来！","Price":"无价之宝",
                                       "Text":'心疼的抱住聪明可爱机智善良勇敢无谓天生丽质霸气侧漏邪魅狂拽智商超群极具魅力温文尔雅风度翩翩彬彬有礼天下无双眉清目秀吹弹可破人面桃花英俊潇洒器宇不凡玉树临风仪表堂堂风流倜傥面如冠玉风度翩翩美目盼兮清新君逸酷到爆的小仙女'})


def results(request):
    return render(request, 'results.html',{"judge":"none"})

def mainPage(request):
    return render(request, 'mainPage.html')