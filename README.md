docker build -t dushyant1334/llama38b:latest . (build image)


docker run -d -p 8501:8501 \
-e AWS_ACCESS_KEY_ID="" \
-e AWS_SECRET_ACCESS_KEY="" \
-e AWS_REGION="ap-south-1" \
dushyant1334/llama38b:latest


docker ps
docker images -a
docker stop conatiner_id

docker rm $(docker ps -a -q) #remove all containers

docker login
docker push dushyant1334/llama38b:latest

docker rmi -f $(docker images -q) #Delete all docker images

docker pull dushyant1334/llama38b

docker run -d -p 8501:8501 \
-e AWS_ACCESS_KEY_ID="" \
-e AWS_SECRET_ACCESS_KEY="" \
-e AWS_REGION="ap-south-1" \
dushyant1334/llama38b:latest



#create virtual env 
pwd
/Users/dushyantsharma/Desktop/awsfreetier/awsbedrock
python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv (make a virutal env)
source /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv/bin/activate (activate virutal env)

pip install -r requirements.txt 

#go to iam console to create user and create access key

Purchased LLama3:8B instruct to work
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
