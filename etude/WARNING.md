MondoDB doesn't seem to have fully general exchange between MongoDB 2.0.x and 
subsequent versions 2.2.x 

The scripts etude_dump/etude_restore produce a dump directory which is presently 
in MongoDB 2.0.x format.  This is unlike to import into MongoDB 2.2.x 

The scripts etude_export/etude_import produce JSON files in the data directory. 
JSON is a subset of BSON, so it's possible that these files contain less 
than the original database.  For these etudes which use simple data structures, 
this is most likely not a concern. 
 
Run the depcheck script to check MongoDB version. 


