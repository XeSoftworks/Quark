
'''
 Xe Softworks 2022                                                                                                 
                             :~!!:                                                                  
                          ~YB&@@@&Y                                                                 
                        !B@@@@@@@@@G:                                                               
                       .&@@@@@@@@@@@#^                                                              
                        ?@@@@@@@@@@@@&~                                                             
                         !&@@@@@@@@@@@@7                            .                               
                          ^B@@@@@@@@@@@@J                        ^5##B57^                           
                           .P@@@@@@@@@@@@5                      ?&@@@@@@@G?.                        
                             J@@@@@@@@@@@@G.                   5@@@@@@@@@@@#:                       
                              !&@@@@@@@@@@@B:                :G@@@@@@@@@@@@5.                       
                               ^B@@@@@@@@@@@#~              !&@@@@@@@@@@@@J                         
                                .P@@@@@@@@@@@&!            J@@@@@@@@@@@@#~                          
                                  J@@@@@@@@@@@@?         .P@@@@@@@@@@@@P.                           
                                   !&@@@@@@@@@@@Y       ^B@@@@@@@@@@@@J                             
                                    ^B@@@@@@@@@@@P.    7&@@@@@@@@@@@#~                              
                                     .P@@@@@@@@@@@B^  J@@@@@@@@@@@@P:                               
                                       J@@@@@@@@@@@&?P@@@@@@@@@@@&?                                 
                                        !&@@@@@@@@@@@@@@@@@@@@@@B^                                  
                                         ^B@@@@@@@@@@@@@@@@@@@@5.                                   
                                          .5@@@@@@@@@@@@@@@@@&7                                     
                                            Y@@@@@@@@@@@@@@@G^                                      
                                             G@@@@@@@@@@@@@B.                                       
                                             B@@@@@@@@@@@@@G                                        
                                           .P@@@@@@@@@@@@@@@5                                       
                                          ^B@@@@@@@@@@@@@@@@@G:                                     
                                         7&@@@@@@@@@@@@@@@@@@@#^                                    
                                        Y@@@@@@@@@@@@@@@@@@@@@@&!                                   
                                      :G@@@@@@@@@@@&#@@@@@@@@@@@@?                                  
                                     ~#@@@@@@@@@@@P: J@@@@@@@@@@@@J                                 
                                    ?@@@@@@@@@@@@Y    ?@@@@@@@@@@@@5.                               
                                  .5@@@@@@@@@@@@?      !&@@@@@@@@@@@G:                              
                                 :G@@@@@@@@@@@&!        ^#@@@@@@@@@@@B:                             
                                !&@@@@@@@@@@@B^          :B@@@@@BY!~~~:                             
                               J@@@@@@@@@@@@P.            :G@@B~  7GB#P~                            
                             .5@@@@@@@@@@@@Y               .GG.  Y@@@@@&.                           
                            ^B@@@@@@@@@@@@?                 ..   !777777.                           
                           !&@@@@@@@@@@@&!                      .?JJJJJJYYY?                        
                          7@@@@@@@@@@@@#^                        G@@@@@@@@@@Y                       
                         J@@@@@@@@@@@@B:                         :B@@@@@@&?^GY                      
                        Y@@@@@@@@@@@@G.                            !J55Y7:.J&@Y                     
                       Y@@@@@@@@@@@@P.                            .^::^~75&@@@@J                    
                      ^@@@@@@@@@@@@P                               5@@@@@@@@@@@@~                   
                       Y#@@@@@@@@@P.                                5@@@@@@@@@@B:                   
                        .~!?JJYYY!                                   ~J55YYYY?~.      

https://xesoft.works
'''
import threading
from wrapper import *

threads = []
f = open('valid.txt', 'a+')

def check(token):
    dc = Discord(str(token.rstrip()))
    output = dc.check_token()

    print(output)
    
    if output['status'] == 'Valid': 
        f.write('{token}\n'.format(token=output['token']))

def main():
    for token in open('tokens.txt', 'r').readlines():
        threads.append(
            threading.Thread(target=check, args=(token.strip(),))
        )

    for t in threads: t.start()
    for t in threads: t.join()

    f.close()

if __name__ == '__main__':
    main()