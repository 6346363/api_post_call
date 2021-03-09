import json
import os

def lambda_handler(event, context):
    
    try:
        path = event['image_path']
        print(path)
        
        extension = os.path.splitext(path)
        print(extension)
    
    except:
        print("exception")
        return {
            'success': 'false',
            'message':"Error:E50012",
            'estimated_data':{}
        }       
    
    if extension is None:
        print("None")
        return {
            'success': 'false',
            'message':"Error:E50012",
            'estimated_data':{}
        }
    else:
        # 拡張子のチェック
        if extension[1] == '.jpg':
            print("jpg file")
            return {
                'success': 'true',
                'message':"success",
                'estimated_data':{
                    'class':3,
                    'confidence':0.8683
                }
            }
        else:
            print("None jpg file")
            return {
                'success': 'false',
                'message':"Error:E50012",
                'estimated_data':{}
                }