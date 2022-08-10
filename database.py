import os

import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
#'auth': 'KERBEROS', 'kerberos_service_name': 'impala'

# https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a

# tryde-manager0.try01cdp.rzqg-cft2.cloudera.site/;ssl=true;transportMode=http;httpPath=tryde/cdp-proxy-api/hive
#jdbc:impala://trydwrt-master0.try01cdp.rzqg-cft2.cloudera.site:443/;ssl=1;transportMode=http;httpPath=trydwrt/cdp-proxy-api/impala;AuthMech=3;

connect_args={'database':'default',
                             'timeout':20,
                             'use_ssl':True,
                             'use_http_transport': True,
                             'http_path': 'trydwrt/cdp-proxy-api/impala',
                             'user':'jprosser', 
                             'password':"BadPass#1",
                             'auth_mechanism':'LDAP'
             }

engine = create_engine('impala://trydwrt-master0.try01cdp.rzqg-cft2.cloudera.site:443', 
                       connect_args=connect_args)
 
#conn = engine.connect()
#ResultProxy  = conn.execute("SELECT * FROM default.pysparktab LIMIT 3")
#print(ResultProxy.fetchall())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

