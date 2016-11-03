def qQuestions(user,password,option):
    from sqlalchemy import create_engine, Column, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, scoped_session 
    
    # Base = declarative_base()
    Base = declarative_base()
    
    class qQuestions(Base):
        __tablename__ = 'qQuestions'
        questionNo = Column(integer(10), primary_key=True, autoincrement=True)
        courseCode = Column(varchar(15),collation=utf8_general_ci)
        questionGroup = Column(varchar(32),collation=utf8_general_ci)
        imgData = Column(blob)
        description = Column(text,collation=utf8_general_ci)
        remarks = Column (varchar(2048),collation=utf8_general_ci)
        hasParams = Column(tinyint(1))
        hasCompositeFIB = Column(tinyint(1))
        hasCompositeMCMR = Column(tinyint(1))
        hasCompositeSA = Column(tinyint(1))


        def __init__(self,questionNo=None,courseCode,questionGroup,imgData=None,description,remarks=None,hasParams=0,hasCompositeFIB=None,hasCompositeMCMR=None,hasCompositeSA=None):
            """Constructor"""
            if questionNo:
                self.questionNo=questionNo
            self.courseCode=courseCode
            self.questionGroup=questionGroup
            self.imgData=imgData
            self.description=description
            self.remarks=remarks
            self.hasParams=hasParams
            self.hasCompositeFIB=hasCompositeFIB
            self.hasCompositeMCMR=hasCompositeMCMR
            self.hasCompositeSA=hasCompositeSA
            
        def __repr__(self):
            """Show this object (database record)"""
            return "<User(%d, %s)>" % (
            self.questionNo, self.courseCode,self.questionGroup)
        
    # Create a database engine
    engine = create_engine('mysql://testuser:12345678@localhost:3306/testdb')
    engine.echo = True  # Echo output to console for debugging
    
    # Drop all tables mapped in Base's subclasses
    #Base.metadata.drop_all(engine)
    
    # Create all tables mapped in Base's subclasses
    Base.metadata.create_all(engine)
    
    # Create a database session binded to our engine, which serves as a staging area
    # for changes to the objects. To make persistent changes to database, call
    # commit(); otherwise, call rollback() to abort.
    Session = scoped_session(sessionmaker(bind=engine))
    dbsession = Session()