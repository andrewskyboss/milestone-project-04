# Database Schema:

- The database "The CUBE | GYM & Fitness Club" For the Merchandise Products will contain 2 collections: Categories, Products


## Categories collection:

Schema

  {

    "_id"             :    <ObjectID>
    "pk"              :    <integer>
    "model"           :    <string>
    "name"            :    <string>
    "friendly_name"   :    <string>

  }

Example

  {

    "_id"             :    <ObjectID>
    "pk"              :    1
    "model"           :    "products.category"
    "name"            :    "activewear"
    "friendly_name"   :    "Activewear"

  }


## Products collection:

Schema

  {

    "_id"               :    <ObjectID>
    "pk"                :    <integer>
    "model"             :    <string>
    "sku"     		    :    <string>
    "name"      	  	:    <string>
    "description" 		:    <string>
    "price"       		:    <decimal>
    "category"          :    <integer>
    "image_url"      	:    <string>
    "image"     		:    <string>

  }

Example

  {

    "_id"               :    <ObjectID>
    "model"      		:    "products.product"
    "sku"   			:    "pp5007160030"
    "name"    			:    "Levrone Levro ISO whey *100% Whey Protein Isolate*"
    "description" 		:    "Premier Quality Whey Protein Isolate"
    "price"         	:    51.99
    "category"         	:    7
    "image_url"       	:    "https://ibb.co/LddMPgK"
    "image"       		:    "levrone-levro-iso-whey-2270-g-1000x1000.jpg"

  }

- The database "The CUBE | GYM & Fitness Club" For the Employee will contain 2 collections: Role, Employee


## Role collection:

Schema

  {

    "_id"   			:    <ObjectID>
    "pk"     			:    <integer>
    "model" 			:    <string>
    "name" 				:    <string>
    "friendly_name" 	:    <string>

  }

Example

  {

    "_id"   			:    <ObjectID>
    "pk"     			:    1
    "model" 			:    "employees.role"
    "name" 				:    "fitness_instructor"
    "friendly_name" 	:    "Fitness Instructor"

  }


## Employee collection:

Schema

  {

    "_id"               :    <ObjectID>
    "pk"        		:    <integer>
    "model"        		:    <string>
    "sku"     			:    <string>
    "name"      		:    <string>
    "role"        		:    <integer>
    "description" 		:    <string>
    "start_date"   		:    <string>
    "qualifications" 	:    <string>
    "interests" 		:    <string>
    "more" 				:    <string>
    "image_url"      	:    <string>
    "image"     		:    <string>

  }

Example

  {

    "_id"               :    <ObjectID>
    "model"      		:    "employees.employee"
    "sku"   			:    "ee00000101"
    "name"    			:    "Jason Travers"
    "role"	         	:    1
    "description" 		:    "Get a better basic tee in a size that"
    "start_date"   		:    "April 2019"
    "qualifications" 	:    "NCEF certified fitness instructor and personal trainer"
    "interests" 		:    "Jason loves all types of training"
    "more"	         	:    ""
    "image_url"       	:    "https://ibb.co/P9mVzzt"
    "image"       		:    "coach-02.jpg"

  }