
    import pandas as pd                                                                              #calling the library

 
 
 
 
    df = pd.read_csv('result.csv', sep = ',')                                                        #take data from csv file

 
 
 
    mf = df.groupby(['Protocol', 'Source', 'Dest_port', 'Sour_port']).count()                        #group the columns
 
 
 
    df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25, 26, 27, 28 ]                                              #indexing

 
 
 
    df.index.name = '№'                                                                              #give the name of the index column


  
  
  
    df.drop(['No.', 'Destination','Time'], axis='columns')                                           #remove too much


   
   
   
    df.to_csv('file_after_processing.csv')                                                           #save the masterpiece


