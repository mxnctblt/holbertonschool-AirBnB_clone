# AirBnB clone

![hbnb](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055856Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=406c7aa5e09ae14afc09ea1d5093e3cbfa0cb8cb89d9ecac027269a5cc993422)

This project has for goal to create a simple copy of the [AirBnB website](https://www.airbnb.com/).
It will not have all the features, only some of them to cover all fundamental concepts of the higher level programming track.

This project will take four months and six steps. We are currently working on: __the Console__


## 1st step - The Console

![console](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T132500Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fdcf5880bb0b118434f6a7e00c369a8a3145fb4b430af45abefe9b1aa156321e)

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### Learning Objectives:
    - Serialization / Deserialization flow (object <-> Dict <-> Json <-> file)
        - Packages / Modules / Cyclical imports / How to import / Prevent execution /Etc.
	    - Layered architecture
	        - Interfaces (storage)
		    - Abstract Classes (BaseClass)

### How to start it:
### How to use it:
### Examples:
## 2nd step - Web static

![webstatic](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055911Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ac1fd9c184178bd3bdacad95a59f2edb39cfe8885b9b6363e5f33b5c9535e0f8)
- learn HTML/CSS
- create the HTML of your application
- create template of each object

## 3rd step - MySQL storage

![mysqlstorage](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055911Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=681160c28d6fa598b05fa45f9ba92267cd59b50f196f395743511a921811d9e3)

- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

## 4th step - Web framework - templating

![webframework](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055911Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b8302dcd4ae2aebd188ad984b731d21ab07d555e05e0e272404171b25ee2d5cc)

- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

## 5th step - RESTful API

![resfulapi](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055911Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1921c9e4406fe7509cb0183804114bcc35edccc5c8c52b0652df918f6bcd1446)

- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

## 6th & last step - Web dynamic

![webdynamic](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230220%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230220T055911Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=550c112375878d1a664576be972e84743f726fb58e8569abe99ea1ab87458228)

- learn JQuery
- load objects from the client side by using your own RESTful API

## Authors:
Antoine Jacob <[AntoineJacob](https://github.com/AntoineJacob)>
& Maxence Thibault <[mxnctblt](https://github.com/mxnctblt)>