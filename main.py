import segno # type: ignore
import os

def create_incremented_filename(base_name, extension):
    counter = 1
    file_name = f"{base_name}{counter}.{extension}"
    while os.path.exists(file_name):
        counter += 1
        file_name = f"{base_name}{counter}.{extension}"
    return file_name

print("""
                                                                            
                                                                                
                                &,             .%                               
                            &&&                   &&&                           
                          & &&                     %&.&                         
                       &  & &                       &#&. &                      
                      &&/ & &                       %%&. &&                     
                     &&.& & &                       & & &.#&                    
                     &&&&&,&%&                     #&&& &&&&                    
                    & &&&&&&&                       & &&&&% /                   
                    &&& &(& &                       %#&%& %&,                   
                     &(.&%&&& &            &      & &&&&&% &                    
                     &&%&&&&#& &&     ,&&%&     && && &&& &%                    
                        &&..& &(&&&& . *& &  &&&%.& &. &&/                      
                        &&&&, &  &&&%  &  & %&&&.&&.#&&&&                       
                          && .&&(%&&&&&,&&&&%&& &&&% &&                         
                             %&&   &/(%&&&  &&.  &&#                            
                                      & &,&   .                                 
                                     &/&&&%&                                    
                                    &&&&& &&&                                   
                                   &&&&&&&&&&&                                  
                                    &&&&&&&&&                                   
                                    & &,&%& &                                   
                                     && & &&(                                   
                                      & & ,                                     
                                        &                                       
                                                                                
""")
print("""
________   __________        _________  ________   ________   ___________                          
\_____  \  \______   \       \_   ___ \ \_____  \  \______ \  \_   _____/                          
 /  / \  \  |       _/       /    \  \/  /   |   \  |    |  \  |    __)_                           
/   \_/.  \ |    |   \       \     \____/    |    \ |    `   \ |        \                          
\_____\ \_/ |____|_  /        \______  /\_______  //_______  //_______  /                          
  ________>___________ _______   _____________________    _____   ___________________   __________ 
 /  _____/ \_   _____/ \      \  \_   _____/\______   \  /  _  \  \__    ___/\_____  \  \______   \ 
/   \  ___  |    __)_  /   |   \  |    __)_  |       _/ /  /_\  \   |    |    /   |   \  |       _/
/    \_\  \ |        \/    |    \ |        \ |    |   \/    |    \  |    |   /    |    \ |    |   \ 
\______  //_______  /\____|__  //_______  / |____|_  /\____|__  /  |____|   \_______  / |____|_  /
        \/         \/         \/         \/         \/         \/                    \/         \/ 
""")
print('Made by Alp')
print('GitHub = https://github.com/Talkzy-py')

Link = input('What is the link that you would like to turn into a QR Code? ')
qrcode = segno.make(Link)
file_name = create_incremented_filename('YourQRCode', 'png')
qrcode.save(file_name)

print(f"QR code saved as: {file_name}, You can find it in the directory you ran this program in!")
