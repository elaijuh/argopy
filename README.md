# ARGOPY

### Introduction

This software is a Python interface to [Argo BBS](http://argolab.org/). It helps developers to access [Argo BBS API](http://argolab.org/api/index.html) via python. You may find [argolab/jsbbs](https://github.com/argolab/jsbbs) in github.

### Install

You should have python 2.6+  

    python setup.py install
   
or just copy/paste `argo.py` to your working directory.

### Usage

Demo code:

    import argo
    
    client = argo.APIClient(domain = 'argolab.org')
    
    # get board name
    o = client.get_ajax_board_alls()['data']  
    for s in o:
        print s['secname'].encode('gbk')
        for b in s['boards']:
            print '    {} {}'.format(b['title'].encode('gbk'), b['boardname'])
            
    # post login
    client.post_ajax_login(userid = 'foo', passwd = 'bar')
    
### Author

- [@mopodo](https://github.com/mopodo)

### License

---
Copyright 2012 mopodo

Licensed under the MIT License