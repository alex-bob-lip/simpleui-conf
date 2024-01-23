#1
from pysimplebase import SimpleBase,DBSession
from ru.travelfood.simple_ui import SimpleUtilites as suClass
from ru.travelfood.simple_ui import ImportUtils as iuClass
import json
import random
import uuid

#creatig database. replase database name with your specified name
db = SimpleBase("generator_test",path=suClass.get_simplebase_dir())

def OnStartInnerOrders(hashMap, *args):
    print("OnStart")
    hashMap.put("return_selected_data","")
    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True,
              "override_search":True

            },
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [ ]
                }

    }
    }
    field_elements=[]
    line ={
          "type": "LinearLayout",
          "orientation": "horizontal",
          "height": "wrap_content",
          "width": "match_parent",
          "weight": "1",
          "Elements": [
		  {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "    № ЛТК000000123 от 12.12.2023    ",
            "TextBold": True,
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "gravity_horizontal": "center"
          },
		  {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@sum",
                    "height": "wrap_content",
                    "width": "match_parent",
					"TextBold": True,
					"TextSize": 16,
                    "weight": "3",
                    "gravity_horizontal": "right"
          }]
          }
    field_elements.append(line)
    line = {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
               {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "Заказчик: ",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "3",
                    "gravity_horizontal": "left"
                },
                {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@order_open",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "1",
                    "TextBold": True,
                    "gravity_horizontal": "left"
                }

                ]
                }
    field_elements.append(line)
    
    line = {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
               {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "Статусы: ",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "3",
                    "gravity_horizontal": "left"
                },
				{
					"type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "1",
                    "Elements": [
                    {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "!!!",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "3",
                        "TextBold": True,
					    "TextColor": "#E8F5E9",
                        "BackgroundColor": "#D81B60",
                        "gravity_horizontal": "center"
                    },
                    {

                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@status",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "1",
                        "TextBold": True,
					    "TextColor": "#E8F5E9",
                        "BackgroundColor": "#4b830d",
                        "gravity_horizontal": "left"
                    }]
				}
            ]
    }
    
    
    field_elements.append(line)
    j["customcards"]["layout"]["Elements"] = field_elements
    j["customcards"]["cardsdata"]=[]
    
    c =  {
          "key": "0",
          "order_open": "Труболитейный цех",
		  "sum": "100000.00",
          "status": " ✅ Директор"
      }
    j["customcards"]["cardsdata"].append(c)  
    c =  {
          "key": "1",
          "order_open": "Цех по ремонту оборудования и оснастки",
		  "sum": "1000000.00",
          "status": " ✅ Начальник"
      }
    j["customcards"]["cardsdata"].append(c)
    hashMap.put("cards",json.dumps(j,ensure_ascii=False))
    
    
    hashMap.put("RefreshScreen","")
    print("onStart - finish2")
    return hashMap

    
    
def set_class_list(hashMap,*args):
    hashMap.put("return_selected_data","")
    
    classname = args[0]

    searchstring=None
    
    if len(args)>2:
       arg = args[2]
       if arg=="search":
          searchstring=str(hashMap.get("SearchString"))
        

    jclass = json.loads(suClass.getClassByName(classname))
    
    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True,
              "override_search":True

            },
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [ ]
                }

    }
    }
    
    

    field_elements=[]
    indexed = False
    for rkey, value in jclass.items():
        if rkey=="_id":
            continue
        if rkey=="_index":
            indexed = True
            continue
          
        if rkey[0]=="_":
            continue
        
        if value[0]=="_":
            continue
        
        if "(" in rkey and ")" in rkey:
            title = rkey[rkey.find("(")+1:rkey.find(")")]
            key = rkey.partition('(')[0]   
        else:
             title = rkey
             key = rkey 


        if isinstance(value, list):     
            continue  
        
        

        if len(title)>0:      
          line =     {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
               {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": title+" : ",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "2",
                    "gravity_horizontal": "left"

                    
                   
                },
                {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@"+key,
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "1",
                    "TextBold": True,
                    "gravity_horizontal": "left"
                }

                ]
                }
          field_elements.append(line)
        else:
          line =  {

                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@"+key,
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "1",
                    "TextBold": True,
                    "gravity_horizontal": "left"
                }

          field_elements.append(line)    
   
    j["customcards"]["layout"]["Elements"] = field_elements

    j["customcards"]["cardsdata"]=[]
    if indexed:
        db[classname].register_text_index(classname + "_text_index", "_index", dynamic = True)
        db[classname].reindex_text(classname + "_text_index")     
    collection = db[classname]

    if searchstring==None:
     result = collection.all()
     
    else:
     
    #  slist = [] 

    #  for rkey, value in jclass.items():
    #     if rkey=="_id":
    #          continue
    #     if rkey[0]=="_" :
    #          continue
        
    #     if isinstance(value, list):     
    #        continue
        
    #     if "(" in rkey and ")" in rkey:
    #         title = rkey[rkey.find("(")+1:rkey.find(")")]
    #         key = rkey.partition('(')[0]   
    #     else:
    #          title = rkey
    #          key = rkey 

    #     if "*" in value:
    #        slist.append({key:{'$regex': searchstring}})     


     #result = collection.find({ "$name_1_description_1": { "$search": searchstring } })  
      result = db[classname + "_text_index"].search_text_index(searchstring.lower()) 
     

    for item in result:
      c =  {
          "key": str(item.get("_id"))
      }

      for rkey, value in jclass.items():
        #if rkey=="_id":
        #     continue
        if rkey[0]=="_" and rkey!="_id":
             continue
        
        if "(" in rkey and ")" in rkey:
            title = rkey[rkey.find("(")+1:rkey.find(")")]
            key = rkey.partition('(')[0]   
        else:
             title = rkey
             key = rkey 

        if key in item:               
          c[key]=str(item.get(key,""))
      
      j["customcards"]["cardsdata"].append(c)

    hashMap.put("cards",json.dumps(j,ensure_ascii=False))
    
    
    hashMap.put("RefreshScreen","")

    return hashMap


def set_container_list(hashMap,*args):
    hashMap.put("return_selected_data","")
    
   

    if hashMap.containsKey("closing"):
       hashMap.put("closing","")
    else:

      classname = args[0]
      property = args[1]

      hashMap.put("nested_property",str(property))

    

      jclass = json.loads(suClass.getClassByName(classname))

      
      
      j = { "customcards":         {
              "options":{
                "search_enabled":True,
                "save_position":True
              },
              "layout": {
                  "type": "LinearLayout",
                  "orientation": "vertical",
                  "height": "wrap_content",
                  "width": "match_parent",
                  "weight": "1",
                  "Elements": [ ]
                  }

      }
      }

      field_elements=[]

      for rkey, value in jclass.items():
          if rkey=="_id":
              continue
          if rkey[0]=="_":
              continue
          
          if "(" in rkey and ")" in rkey:
              title = rkey[rkey.find("(")+1:rkey.find(")")]
              key = rkey.partition('(')[0]   
          else:
              title = rkey
              key = rkey 

          if isinstance(value, list):     
            continue

          if len(title)>0:      
            line =     {
                  "type": "LinearLayout",
                  "orientation": "horizontal",
                  "height": "wrap_content",
                  "width": "match_parent",
                  "weight": "1",
                  "Elements": [
                {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": title+" : ",
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "2",
                      "gravity_horizontal": "left"

                      
                    
                  },
                  {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": "@"+key,
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "1",
                      "TextBold": True,
                      "gravity_horizontal": "left"
                  }

                  ]
                  }
            field_elements.append(line)
          else:
            line =  {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": "@"+key,
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "1",
                      "TextBold": True,
                      "gravity_horizontal": "left"
                  }

            field_elements.append(line)    
    
      j["customcards"]["layout"]["Elements"] = field_elements

      j["customcards"]["cardsdata"]=[]

      #jobject =json.loads(hashMap.get("object"))

      if hashMap.containsKey("object_"+str(hashMap.get("current_screen_name"))):

        jobject = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))


        
        if property in jobject:
        
          result = jobject.get(property)
          

          for item in result:
            c =  {
                "key": str(item.get("_id"))
            }

            for rkey, value in jclass.items():
              if key=="_id":
                  continue
              if rkey[0]=="_":
                  continue
              
              if isinstance(value, list):     
                  continue

              
              if "(" in rkey and ")" in rkey:
                  title = rkey[rkey.find("(")+1:rkey.find(")")]
                  key = rkey.partition('(')[0]   
              else:
                  title = rkey
                  key = rkey 

              if key in item:               
                c[key]=str(item.get(key,""))
            
            j["customcards"]["cardsdata"].append(c)

      #if not hashMap.containsKey("cards"):
      
      hashMap.put("cards",json.dumps(j,ensure_ascii=False))
      
      hashMap.put("RefreshScreen","")

    return hashMap


def set_container_list_ref(hashMap,*args):
    
    if hashMap.containsKey("update_nested_property"):
        classname = hashMap.get("update_nested_property")
        hashMap.remove("update_nested_property")

        jcurrent_object = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
        jselected_object=json.loads(hashMap.get("selected_card_data"))

        if not hashMap.get("nested_property") in jcurrent_object:
          jcurrent_object[hashMap.get("nested_property")]=[]

        jcurrent_object[hashMap.get("nested_property")].append(jselected_object.get("_id"))

        
        collection = db[classname]
        post_id = collection.insert(jcurrent_object,upsert=True)
        jcurrent_object["_id"]=str(post_id)
        

        hashMap.put("object_"+str(hashMap.get("current_screen_name")),json.dumps(jcurrent_object,ensure_ascii=False))
    
    if hashMap.containsKey("closing"):
       hashMap.put("closing","")
    else:

      classname = args[0]
      property = args[1]

      hashMap.put("nested_property",str(property))

    

      jclass = json.loads(suClass.getClassByName(classname))

      
      
      j = { "customcards":         {
              "options":{
                "search_enabled":True,
                "save_position":True
              },
              "layout": {
                  "type": "LinearLayout",
                  "orientation": "vertical",
                  "height": "wrap_content",
                  "width": "match_parent",
                  "weight": "1",
                  "Elements": [ ]
                  }

      }
      }

      field_elements=[]

      for rkey, value in jclass.items():
          if rkey=="_id":
              continue
          if rkey[0]=="_":
              continue
          
          if "(" in rkey and ")" in rkey:
              title = rkey[rkey.find("(")+1:rkey.find(")")]
              key = rkey.partition('(')[0]   
          else:
              title = rkey
              key = rkey 

          if isinstance(value, list):     
            continue

          if len(title)>0:      
            line =     {
                  "type": "LinearLayout",
                  "orientation": "horizontal",
                  "height": "wrap_content",
                  "width": "match_parent",
                  "weight": "1",
                  "Elements": [
                {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": title+" : ",
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "2",
                      "gravity_horizontal": "left"

                      
                    
                  },
                  {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": "@"+key,
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "1",
                      "TextBold": True,
                      "gravity_horizontal": "left"
                  }

                  ]
                  }
            field_elements.append(line)
          else:
            line =  {

                      "type": "TextView",
                      "show_by_condition": "",
                      "Value": "@"+key,
                      "height": "wrap_content",
                      "width": "match_parent",
                      "weight": "1",
                      "TextBold": True,
                      "gravity_horizontal": "left"
                  }

            field_elements.append(line)    
    
      j["customcards"]["layout"]["Elements"] = field_elements

      j["customcards"]["cardsdata"]=[]

      #jobject =json.loads(hashMap.get("object"))

      if hashMap.containsKey("object_"+str(hashMap.get("current_screen_name"))):

        jobject = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))

        collection = db[classname]

     
        if property in jobject:
        
          result = collection.find({"_id":{"$in":jobject[property]}})
          

          for item in result:
            c =  {
                "key": str(item.get("_id"))
            }

            for rkey, value in jclass.items():
              if key=="_id":
                  continue
              if rkey[0]=="_":
                  continue
              
              if isinstance(value, list):     
                  continue

              
              if "(" in rkey and ")" in rkey:
                  title = rkey[rkey.find("(")+1:rkey.find(")")]
                  key = rkey.partition('(')[0]   
              else:
                  title = rkey
                  key = rkey 

              if key in item:               
                c[key]=str(item.get(key,""))
            
            j["customcards"]["cardsdata"].append(c)

      #if not hashMap.containsKey("cards"):
      
      hashMap.put("cards",json.dumps(j,ensure_ascii=False))
      
      hashMap.put("RefreshScreen","")

    return hashMap


def open_object(hashMap,*args):
    
    #hashMap.put("toast",str(hashMap.get("current_process_name")))
    hashMap.put("return_selected_data","")

    if hashMap.containsKey("closing"):
       hashMap.remove("closing")
    elif hashMap.containsKey("result_back"):
       hashMap.remove("result_back")   
    else:

      if hashMap.containsKey("selected_card_key"):
        hashMap.remove("selected_card_key")

        
      
      classname = args[0]
      form_name = hashMap.get("current_screen_name")

      jclass = json.loads(suClass.getClassByName(classname))

      refobjects=[]

      if hashMap.containsKey("object_"+form_name):

        jobject = json.loads(hashMap.get("object_"+form_name))

        for rkey, value in jclass.items():
            if rkey=="_id":
                continue
            if rkey[0]=="_":
                continue
            
             

            if "(" in rkey and ")" in rkey:
                title = rkey[rkey.find("(")+1:rkey.find(")")]
                key = rkey.partition('(')[0]   
            else:
                title = rkey
                key = rkey      

            if "_ref" in value:
               refobjects.append(key)   

            if hashMap.containsKey(key):
              hashMap.remove(key)

        for key,value in jobject.items():
          if  isinstance(value,dict):
              hashMap.put(key+"_view",value.get("name"))
              hashMap.put(key,json.dumps(value,ensure_ascii=False))
          elif key in refobjects:
              hashMap.put(key+"_view","по ссылке") 
          elif key=="_id" or key=="id":  
             continue   
          else:
            if not isinstance(value,list):
              hashMap.put(key,value)


    return hashMap



def open_object_form(hashMap,*args):
    
    hashMap.put("disable_events","")
    hashMap.put("return_selected_data","")
    
    classname = args[0]
    form_name = args[1]
    if len(args)>2:
      oper = args[2]
    else:
      oper=None   

    if hashMap.containsKey("object_"+str(hashMap.get("current_screen_name"))):
          hashMap.put("parent_object","object_"+str(hashMap.get("current_screen_name")))
          hashMap.put("parent_class",hashMap.get("parent_class"))

    else:   
          hashMap.put("parent_object","")
          hashMap.put("parent_class",classname)
    
    
    if oper=="?": #добавление
       jclass = json.loads(suClass.getClassByName(classname))
 
       if hashMap.containsKey("selected_card_key"):
          hashMap.remove("selected_card_key")

       hashMap.put("object_"+form_name,"{}")
      
       hashMap.put("ShowScreen",form_name) 

    elif oper=="??":
       jclass = json.loads(suClass.getClassByName(classname))
  
       if hashMap.containsKey("selected_card_key"):
          jobject = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
          #hashMap.put("toast",json.dumps(item,ensure_ascii=False))
          for item in jobject[hashMap.get("nested_property")]:
            if item['_id']==hashMap.get('selected_card_key'):
              

              hashMap.put("object_"+form_name,json.dumps(item,ensure_ascii=False))

              hashMap.put("ShowScreen",form_name)
              break
          
          
          hashMap.remove("selected_card_key")      
        
      
    else: #формы списков
    
      
      if hashMap.containsKey("selected_card_key"):
        
        
        collection = db[classname]

        #jobject =collection.find_one(hashMap.get("selected_card_key"))
        jobject =collection.get(hashMap.get("selected_card_key"))
        jobject["_id"]=str(jobject["_id"])
      
        hashMap.put("object_"+form_name,json.dumps(jobject,ensure_ascii=False))
        hashMap.put("ShowScreen",form_name)
        
      else:
        
        hashMap.put("object_"+form_name,"{}")   

      

    hashMap.put("noRefresh","")

    return hashMap


def open_object_form_ref(hashMap,*args):
    
    hashMap.put("disable_events","")
    hashMap.put("return_selected_data","")
    
    classname = args[0]
    form_name = args[1]
    if len(args)>2:
      oper = args[2]
    else:
      oper=None   

    if hashMap.containsKey("object_"+str(hashMap.get("current_screen_name"))):
          hashMap.put("parent_object","object_"+str(hashMap.get("current_screen_name")))
          hashMap.put("parent_class",hashMap.get("parent_class"))

    else:   
          hashMap.put("parent_object","")
          hashMap.put("parent_class",classname)
    
    
    if oper=="?": #добавление
       jclass = json.loads(suClass.getClassByName(classname))
 
       if hashMap.containsKey("selected_card_key"):
          hashMap.remove("selected_card_key")

       hashMap.put("object_"+form_name,"{}")

       hashMap.put("ShowScreen",form_name)
       hashMap.put("_key","add_res")
       hashMap.put("result_process",hashMap.get("current_process_name"))
       hashMap.put("result_screen",hashMap.get("current_screen_name"))
       hashMap.put("update_nested_property",classname)
       

      
       #hashMap.put("ShowProcessResult",form_name) 
       #hashMap.put("SetResultListener","cell_res") 

    elif oper=="??":
       jclass = json.loads(suClass.getClassByName(classname))
  
       if hashMap.containsKey("selected_card_key"):
          jobject = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
          hashMap.put("toast",json.dumps(jobject,ensure_ascii=False))
          for item in jobject[hashMap.get("nested_property")]:
             
            if str(item)==hashMap.get('selected_card_key'):

              dbname = db

              class_collection = jclass.get(hashMap.get("nested_property"))
              class_collection_name = class_collection[0].replace("_ref","")
              
              jobject_open = dbname[class_collection_name].get(hashMap.get('selected_card_key'))

              hashMap.put("object_"+form_name,json.dumps(jobject_open,ensure_ascii=False))
              

              hashMap.put("ShowScreen",form_name)

              
              hashMap.put("result_process",hashMap.get("current_process_name"))
              hashMap.put("result_screen",hashMap.get("current_screen_name"))
              
              break
          
          
          hashMap.remove("selected_card_key")      
   
    return hashMap

def save_object(hashMap,*args):
    classname = args[0]

    delete=False
    if len(args)>1:
       delete=True
    
    #hashMap.put("no_clear_hm","")
   
    jclass = json.loads(suClass.getClassByName(classname))
    
    if hashMap.get("parent_object")=="" or hashMap.get("parent_class")==classname:
      
      hashMap.put("ShowScreen","list_form")

      collection_name = classname
      jobject = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))

      if delete:
         
         
         collection = db[collection_name]
         collection.delete(jobject.get("_id"))

         hashMap.remove("object")
         #hashMap.put("BackScreen","")
         hashMap.put("ShowScreen","list_form")
      else:  
        
        index = ""
        for rkey, value in jclass.items():
            if rkey=="_id":
                continue
            if rkey[0]=="_":
                continue
            if rkey=="_index":
                continue  
            
            if "(" in rkey and ")" in rkey:
                title = rkey[rkey.find("(")+1:rkey.find(")")]
                key = rkey.partition('(')[0]   
            else:
                title = rkey
                key = rkey      

            if hashMap.containsKey(key):
              v = hashMap.get(key)
              if "{" in v and "}" in v:
                 jv = json.loads(v)
                 jobject[key]=jv
              else:   
                 jobject[key]=hashMap.get(key)
            if "*" in value:
              index = index + jobject[key]     
        for rkey, value in jclass.items():      
            if "_index" in rkey:
                jobject[rkey] = index.lower()
        
        collection = db[collection_name]
        post_id = collection.insert(jobject,upsert=True)
        jobject["_id"]=str(post_id)

    
    else:
       
       hashMap.put("BackScreen","")

       jcurrent_object = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
       jobject =  json.loads(hashMap.get(hashMap.get("parent_object")))

       collection_name=hashMap.get("parent_class") 
       index = "" 
       for rkey, value in jclass.items():
          if rkey=="_id":
              continue
          if rkey[0]=="_":
              continue
          if rkey=="_index":
              continue   
          
          if "(" in rkey and ")" in rkey:
              title = rkey[rkey.find("(")+1:rkey.find(")")]
              key = rkey.partition('(')[0]   
          else:
              title = rkey
              key = rkey      
          
          if hashMap.containsKey(key):
             v = hashMap.get(key)
             if "{" in v and "}" in v:
                 jv = json.loads(v)
                 jcurrent_object[key]=jv
             else:   
                 jcurrent_object[key]=hashMap.get(key)
             #jcurrent_object[key]=hashMap.get(key) 
          if "*" in value:
            index = index + jobject[key] 
            
       for rkey, value in jclass.items():      
            if rkey=="_index":
                jobject[rkey] = index.lower() 
       if not "_id" in jcurrent_object: #добавление
          jcurrent_object['_id']=  str(uuid.uuid4().hex)

          if not hashMap.get("nested_property") in jobject:
            jobject[hashMap.get("nested_property")]=[]

          jobject[hashMap.get("nested_property")].append(jcurrent_object)
       
       else:   
          objectlist = jobject[hashMap.get("nested_property")]
          for index, item  in enumerate(objectlist):
           if jcurrent_object.get("_id")==item.get("_id"):
            if delete:
              objectlist.pop(index)
             
            else:   
              objectlist[index] = jcurrent_object   
            jobject[hashMap.get("nested_property")]= objectlist
            


            break

            

    

       

       hashMap.put(str(hashMap.get("parent_object")),json.dumps(jobject,ensure_ascii=False))
        

    hashMap.remove("object_"+str(hashMap.get("current_screen_name")))  


    jclass = json.loads(suClass.getClassByName(classname))

    for rkey, value in jclass.items():
        
        if rkey[0]=="_":
             continue
        
        if "(" in rkey and ")" in rkey:
            title = rkey[rkey.find("(")+1:rkey.find(")")]
            key = rkey.partition('(')[0]   
        else:
             title = rkey
             key = rkey      

        if hashMap.containsKey(key):
           hashMap.remove(key) 

        if hashMap.containsKey(key+"_view"):
           hashMap.remove(key+"_view")    
   

    
   
    
    #hashMap.put("closing","")

    return hashMap

def close_without_saving(hashMap,*args):
    classname = args[0]

    hashMap.remove("object_"+str(hashMap.get("current_screen_name")))  


    jclass = json.loads(suClass.getClassByName(classname))

    for rkey, value in jclass.items():
        
        if rkey[0]=="_":
             continue
        
        if "(" in rkey and ")" in rkey:
            title = rkey[rkey.find("(")+1:rkey.find(")")]
            key = rkey.partition('(')[0]   
        else:
             title = rkey
             key = rkey      

        if hashMap.containsKey(key):
           hashMap.remove(key) 

        if hashMap.containsKey(key+"_view"):
           hashMap.remove(key+"_view")    
   
   
    #if hashMap.get("current_screen_name")=="edit_screen":
    #  hashMap.put("ShowScreen","list_form")
    #else:    
    hashMap.put("BackScreen","")
    
    hashMap.put("close","")

    return hashMap

def delete_object(hashMap,*args):
    classname = args[0]
   
    if hashMap.containsKey("nested_object"):
      jobject =json.loads(hashMap.get("nested_object"))
      
      collection = db[classname]
      collection.delete(jobject.get("_id"))

      hashMap.remove("object")
      hashMap.put("BackScreen","")
    elif hashMap.containsKey("object"):
      jobject =json.loads(hashMap.get("object"))
      
      collection = db[classname]
      collection.delete(jobject.get("_id"))

      hashMap.remove("object")
      hashMap.put("BackScreen","")
    

    return hashMap


def start_selection_for_field(hashMap,*args):
    
    

    process =  args[0]  
    screen =  args[1]  
    field =  args[2]  

    #hashMap.put("SwitchProcessScreen",process+"|"+screen)
    hashMap.put("ShowScreen",process+"|"+screen)
    #hashMap.put("SetResultListener",field+"_res")
    hashMap.put("_key",field+"_res")

    hashMap.put("result_process",hashMap.get("current_process_name"))
    hashMap.put("result_screen",hashMap.get("current_screen_name"))



    

    return hashMap


def return_result(hashMap,*args):
    
    
    key =str(hashMap.get("_key"))[:hashMap.get("_key").find("_res")] 
    
       
    #hashMap.put("FinishProcess","")
    #hashMap.put("SwitchProcessScreen",hashMap.get("result_process")+"|"+hashMap.get("result_screen"))
    hashMap.put("ShowScreen",hashMap.get("result_screen"))
    
    hashMap.put(key,hashMap.get("selected_card_data"))
    jcard = json.loads(hashMap.get(key))
    #hashMap.put("return_result_to_",hashMap.get("selected_card_data"))
    hashMap.put("result_back","")
    hashMap.put(key+"_view",jcard.get("name","<noname>"))
    jcurrent_object = json.loads(hashMap.get("object_"+str(hashMap.get("result_screen"))))
    hashMap.put("object_"+str(hashMap.get("current_screen_name")),json.dumps(jcurrent_object,ensure_ascii=False))
    
    hashMap.put("noRefresh","")

    return hashMap

def set_object_value(hashMap,*args):
    key =  args[0] 
    asref =  args[1]  

    #hashMap.put("toast","set_object_value")

    jcard = json.loads(hashMap.get(key))

    v = iuClass.getView(key)
    v.setText(jcard.get("name","noname"))

    hashMap.put(key+"_view",jcard.get("name","noname"))

    jcurrent_object = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
    if asref=="1":
      jcurrent_object[key] = {"_id":jcard["_id"] ,"name": jcard.get("name","noname")}
      hashMap.put(key,json.dumps(jcurrent_object[key],ensure_ascii=False))
    else:  
      jcurrent_object[key] = jcard

    hashMap.put("object_"+str(hashMap.get("current_screen_name")),json.dumps(jcurrent_object,ensure_ascii=False))

    hashMap.put("noRefresh","")

    return hashMap

def add_object_ref(hashMap,*args):
    
    classname =  args[0] 
    selected_object_key =  args[1] 

    jcurrent_object = json.loads(hashMap.get("object_"+str(hashMap.get("current_screen_name"))))
    jselected_object=json.loads(hashMap.get(selected_object_key))

    if not hashMap.get("nested_property") in jcurrent_object:
      jcurrent_object[hashMap.get("nested_property")]=[]

    jcurrent_object[hashMap.get("nested_property")].append(jselected_object.get("_id"))

    
    collection = db[classname]
    post_id = collection.insert(jcurrent_object,upsert=True)
    jcurrent_object["_id"]=str(post_id)
    

    hashMap.put("object_"+str(hashMap.get("current_screen_name")),json.dumps(jcurrent_object,ensure_ascii=False))

    if hashMap.containsKey("noRefresh"):
       hashMap.remove("noRefresh")

    return hashMap

def delete_object_ref(hashMap,*args):
    
    classname =  args[0] 
    

    jcurrent_object = json.loads(hashMap.get(hashMap.get("parent_object")))
    jselected_object=json.loads(hashMap.get("object_"+hashMap.get("current_screen_name")))

    
    for i,item in enumerate(jcurrent_object[hashMap.get("nested_property")].copy()):
      if item == jselected_object['_id']:
        jcurrent_object[hashMap.get("nested_property")].pop(i)
        hashMap.put("speak",str(i))
    
    collection = db[hashMap.get("parent_class")]
    
    updated = jcurrent_object.copy()
    #updated.pop("_id")

    collection.update(jcurrent_object,updated)
   
    hashMap.put(str(hashMap.get("parent_object")),json.dumps(jcurrent_object,ensure_ascii=False))

    if hashMap.containsKey("noRefresh"):
        hashMap.remove("noRefresh")

    hashMap.put("BackScreen","")

    return hashMap
