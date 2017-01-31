from sqlalchemy.sql.sqltypes import SMALLINT, TEXT, Integer, LargeBinary, FLOAT
from sqlalchemy import create_engine, Column, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session 
from sqlalchemy.dialects.mssql.base import TINYINT
from MySQLdb.constants.FIELD_TYPE import VARCHAR
from sqlalchemy.sql.schema import UniqueConstraint, PrimaryKeyConstraint,\
    ForeignKeyConstraint, ForeignKey
from sqlalchemy.dialects import postgresql

def make_QnA():
    # Base = declarative_base()
    Base = declarative_base()
    
    class QnA(Base):
        __tablename__ = 'QnA'
        
        questionNo = Column(Integer, primary_key=True, autoincrement=True)
        imgData = Column(String(256))
        description = Column(TEXT)
        remarks = Column (String(2048))
        ques = Column (postgresql.ARRAY(String(64), dimensions = 2))
        ans = Column (postgresql.ARRAY(String(64), dimensions=2))
        
        def __init__(self,description,questionNo=None,imgData=None,remarks=None,ques=[],ans=[]):
            """Constructor"""
            if questionNo:
                self.questionNo=questionNo 
            self.imgData=imgData
            self.description=description
            self.remarks=remarks
            self.ques=ques
            self.ans=ans
                     
                
        def __repr__(self):
            """Show this object (database record)"""
            return "<User(%d, %s)>" % (
            self.questionNo, self.description)
            
    engine = create_engine('postgresql://testuser:test123@localhost:5432/testdb')
    engine.echo = True  # Echo output to console for debugging
    
    # Drop all tables mapped in Base's subclasses
    Base.metadata.drop_all(engine)
    
    # Create all tables mapped in Base's subclasses
    Base.metadata.create_all(engine)
    
    # Create a database session binded to our engine, which serves as a staging area
    # for changes to the objects. To make persistent changes to database, call
    # commit(); otherwise, call rollback() to abort.
    Session = scoped_session(sessionmaker(bind=engine))
    dbsession = Session()
    
    
    testcases=[{"questionNo":801,"description":"This question does not relate to the image! Suppose that you plucked %%P1%% apples,and Steve took away three. How many apples do you have?"\
                ,"ques":[['1','0','0','five'],['1','1','0','six']],"ans":[['0','0','10','0'],['0','1','11','0'],['0','2','2','1'],['0','3','13','0'],['0','4','14','0'],['1','0','21','0'],\
                                                                          ['1','1','22','0'],['1','2','23','0'],['1','3','24','0'],['1','4','All of the Above','0'],['1','5','None of the Above','1']],"remarks":"Hello 801"},\
               {"questionNo":802,"description":"Which scientist developed the theory of universal gravitation?"\
                ,"ques":[['0','0','0','0'],['0','0','0','0']],"ans":[['0','0','Issac Newtown','0'],['0','1','Charles Darwin','1'],['0','2','Albert Einstein','0'],['0','3','Michael Faraday','0']],"remarks":"Hello 802"}];
                
    for t in testcases:
        dbsession.add(QnA(questionNo=t['questionNo'], description=t['description'], remarks=t['remarks'], ques=t['ques'], ans=t['ans']))
    
    dbsession.commit()
    qQues=dbsession.query(QnA).all()
    return qQues


    