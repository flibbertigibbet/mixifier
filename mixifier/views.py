from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from os import listdir, path, walk
from celery import task
from celery.result import AsyncResult
import afromb
import echonest.remix.audio as audio
from secrets import ECHO_NEST_API_KEY

audio.config.ECHO_NEST_API_KEY = ECHO_NEST_API_KEY

mediadir = default_storage.location
mixdir = path.join(mediadir, 'mix')

@task()
def getMixAnalysis(f1, f2, outf, mix):
    print("analyzing...")
    myAB = afromb.AfromB(f1, f2, path.join(mixdir, outf))
    print("tempo A: " + str(myAB.input_a.analysis.tempo['value']))
    myAB.run(float(mix), True)

@task()      
def makeMix(myAfromB):
    myAfromB.run(mix, True)

def pick(request):
    
    if request.method == 'POST':
        response = request.POST
        
        print(response)
        
        fileOne = path.join(mediadir, response['fileOne'])
        fileTwo = path.join(mediadir, response['fileTwo'])
        mixiness = response['mixiness']
        
        p, f = path.split(response['fileOne'])
        p2, f2 = path.split(response['fileTwo'])
        f = f[:-4]
        f2 = f2[:-4]
        
        outFile = f + '_' + f2 + '_MIXINESS_' + str(float(mixiness) * 10) + '.wav'
            
        print(outFile)
        
        if path.exists(path.join('/media/mix/', outFile)):
            return HttpResponseRedirect(path.join('/media/mix', outFile))# just serve it
        
        analysisTask = getMixAnalysis.apply_async([fileOne, fileTwo, outFile, mixiness])
        taskId = analysisTask.task_id
        
        print("starting analysis for task ID " + str(taskId) + " ...")
        
        return HttpResponseRedirect('/analyze/' + str(taskId) + '/' + outFile)
    else:
        for p, d, f in walk(default_storage.location):
            raw_list = f
            break # don't walk subdirectories
            
        return render(request, 'main_template.html', {'raw_list': raw_list})

def analyze(request, taskid, outf):
    
    t = AsyncResult(taskid)
    print(t.task_id + '\t' + t.status)
    
    if not t.ready():
        return HttpResponse('<html><meta http-equiv="refresh" content="5">' + \
            '<body><img src="/media/mix/mixify.gif" /></body></html>')
    else:
        return HttpResponseRedirect(path.join('/media/mix', outf))
        

    #print("tempo A: " + myAfromB.input_a.analysis.tempo['value'])
    #print("tempo B: " + myAfromB.input_b.analysis.tempo['value'])
    #print("time signature A: " + myAfromB.input_a.analysis.time_signature['value'])
    #print("time signature B: " + myAfromB.input_b.analysis.time_signature['value'])
    #print("mode A: " + myAfromB.input_a.analysis.mode['value'])
    #print("mode B: " + myAfromB.input_b.analysis.mode['value'])
    #print("loudness A: " + myAfromB.input_a.analysis.loudness['value'])
    #print("loudness B: " + myAfromB.input_b.analysis.loudness['value'])

