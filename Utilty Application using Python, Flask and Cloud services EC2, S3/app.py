Jeet Patel
Jeet Patel
11:35 Yesterday
ip address of this project - http://3.6.39.109/
from flask import jsonify, Flask, redirect, render_template, request, url_for
import boto3

app=Flask(__name__)

app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png','jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024

@app.route('/')
def index():
	return render_template('index.html')

iname=""
@app.route('/upload',methods=['GET','POST'])
def uplaod_file():
   if request.method=='POST':
      name = request.form.get('name')
      
      file = request.files['file']
      global iname
      inames = name+"-"+file.filename
      iname = inames.replace(" ","")
      if '.png' in file.filename or '.jpeg' in file.filename:           
         s3 = boto3.client('s3')
         if '.png' in file.filename:
              s3.upload_fileobj(file,'samplebucket-one',Key=iname,ExtraArgs={'ACL': 'public-read',"Metadata": {"mykey": "image/png"}})
         if '.jpeg' in file.filename:
              s3.upload_fileobj(file,'samplebucket-one',Key=iname,ExtraArgs={'ACL': 'public-read',"Metadata": {"mykey": "image/jpeg"}})
        
         
         return redirect(url_for('success'))
      else:
           return redirect(url_for('error')) 

@app.route('/success')
def success():
       bucket_name = 'samplebucket-one'
              
       s3 = boto3.resource('s3')
       bucket = s3.Bucket(bucket_name)
       location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
       url = "https://%s.s3.%s.amazonaws.com/%s" % (bucket_name,location,iname)
       
       return render_template('success.html',link = url)

@app.route('/error')
def error():
	return render_template('error.html') 


@app.route('/display')
def list_files():
    s3 = boto3.client('s3')
    obj = s3.list_objects(Bucket='samplebucket-one')
    contents = []
    for item in s3.list_objects(Bucket='samplebucket-one')['Contents']:
        contents.append(item)
    l=[]
    for i in contents:
         l.append(i.get('Key'))
    l2=[]
    location = boto3.client('s3').get_bucket_location(Bucket='samplebucket-one')['LocationConstraint']
    for i in l:
         url = "https://%s.s3.%s.amazonaws.com/%s" % ('samplebucket-one',location,i)
         l2.append(url)            
    return render_template('display.html',mylist=l2) 
if __name__=='__main__':
	app.run('0.0.0.0','80')
