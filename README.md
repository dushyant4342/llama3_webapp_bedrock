# llama3_webapp_bedrock

#create virtual env 
pwd
/Users/dushyantsharma/Desktop/awsfreetier/awsbedrock
python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv (make a virutal env)
source /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv/bin/activate (activate virutal env)

pip install -r requirements.txt 

#go to iam console to create user and create access key

Purchased LLama3:8B instruct to test
#Llama 3 8B Instruct

<!-- 
{
 "modelId": "meta.llama3-8b-instruct-v1:0",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
} -->

#Sold by: Meta
#Categories: Text summarization, Text classification, Sentiment analysis
#Deployment type: Serverless 

#docker run -d -p 8501:8501 \
#-e AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY" \
#-e AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY" \
#-e AWS_REGION="ap-south-1" \
#llama3-webapp
