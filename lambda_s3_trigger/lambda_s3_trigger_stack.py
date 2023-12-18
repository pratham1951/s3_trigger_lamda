from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications ,
    aws_lambda_event_sources as eventsources,
    Stack
)
from constructs import Construct
 
 
class S3TriggerStack(Stack):
 
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
 
        # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    function_name="s3lamdafunction",
                                    code=_lambda.Code.from_asset("./lambda"))
        
        function2 = _lambda.Function(self, "lambda_function2",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    function_name="s3lamdafunction2",
                                    code=_lambda.Code.from_asset("./lambda"))                            
        # create s3 bucket
        s3 = _s3.Bucket(self, "s3bucketforlamda",bucket_name='mytestbucket-boomi3')
        bucket = _s3.Bucket(self, "Bucket",bucket_name='mytestbucket-boomi4')

        # s3 = _s3.Bucket.from_bucket_attributes(
        #     self, 'LambdaCodeBucket',
        #     bucket_name='mytestbucket-boomi'
        # )
        # bucket = _s3.Bucket.from_bucket_attributes(
        #     self, 'LambdaCodeBucket2',
        #     bucket_name='mytestbucket-boomi2'
        # )

        # function.add_event_source(eventsources.S3EventSource(bucket,
        # events=[_s3.EventType.OBJECT_CREATED]
        # ))
        # function2.add_event_source(eventsources.S3EventSource(bucket2,
        # events=[_s3.EventType.OBJECT_CREATED]
        # ))



 
        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)
 
        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)

         
        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function2)
 
        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        bucket.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)