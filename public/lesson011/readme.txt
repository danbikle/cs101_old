lesson011/readme.txt

redshift

https://us-west-2.console.aws.amazon.com/redshift/home?region=us-west-2

https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html

http://www.sql-workbench.net/Workbench-Build124.zip

unzip...

~/sqlwb/sqlworkbench.sh

out of order:
https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html

https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/1.2.16.1027/RedshiftJDBC42-1.2.16.1027.jar

~/sqlwb/ext/RedshiftJDBC42-1.2.16.1027.jar


https://console.aws.amazon.com/iam/


In the left navigation pane, choose Roles.

Choose Create role

In the AWS Service group, choose Redshift.

Under Select your use case, choose Redshift - Customizable then choose Next: Permissions.

On the Attach permissions policies page, choose AmazonS3ReadOnlyAccess, and then choose Next: Review.

For Role name, type a name for your role. For this tutorial, type myRedshiftRole.

Review the information, and then choose Create Role.

Choose the role name of the role you just created.

Copy the Role ARN to your clipboard

my arn:

arn:aws:iam::448496253599:role/myRedshiftRole

now I should create a cluster:


https://console.aws.amazon.com/redshift/

select US West (Oregon).

choose Quick launch cluster.

On the Cluster specifications page, enter the following values and then choose Launch cluster:

    Node type: Choose dc2.large.

    Number of compute nodes: Keep the default value of 2.

    Master user name: Keep the default value of awsuser.

    Master user password and Confirm password: Enter a password for the master user account.
pass: Dan12345

    Database port: Accept the default value of 5439.

    Available IAM roles: Choose myRedshiftRole.

Cluster redshift-cluster-1 is being created. Your cluster may take a few minutes to launch.



    If you launched your cluster in the EC2-VPC platform, follow the steps in To Configure the VPC Security Group (EC2-VPC Platform).

    If you launched your cluster in the EC2-Classic platform, follow the steps in To Configure the Amazon Redshift Security Group.

I checked my cluster here:

https://us-west-2.console.aws.amazon.com/redshift

I saw this:

Cluster Properties
VPC IDVPC ID of the cluster subnet group associated with this cluster.	
vpc-14eb2d6c ( View VPCs )

So, my cluster is in  the EC2-VPC platform



How to Configure the VPC Security Group (EC2-VPC Platform):

visit
https://us-west-2.console.aws.amazon.com/redshift
choose Clusters.
click redshift-cluster-1

I should land in Configuration tab.

Find my security group

I saw this link:

VPC security groupsList of VPC Security Groups associated with this cluster.	
default (sg-b0e2acc3)
 ( active )

I clicked it

I landed here:

https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#SecurityGroups:search=sg-b0e2acc3;sort=groupId

I clicked the Inbound tab. 

I clicked button: "Edit"

I clicked button: "Add Rule"

I entered the following

    Type: Custom TCP Rule.

    Protocol: TCP.

    Port Range: type the same port number that you used when you launched the cluster. The default port for Amazon Redshift is 5439, but your port might be different.

    Source: select Custom IP, then type 0.0.0.0/0.
I clicked Save.



How To Get Your Connection String

    In the Amazon Redshift console, in the navigation pane, choose Clusters.

    Choose redshift-cluster-1 to open it, I should land in the Configuration tab.

    I copied the JDBC URL of the cluster:
    
jdbc:redshift://redshift-cluster-1.cmea74qjjc8h.us-west-2.redshift.amazonaws.com:5439/dev    



how To Connect from SQL Workbench/J to Your Cluster

    Open SQL Workbench/J.

    Choose File, and then choose Connect window.

    Choose Create a new connection profile.

    In the New profile text box, type a name for the profile.

    Choose button "Manage Drivers" at bottom. The Manage Drivers dialog should open.

    Choose the Create a new entry button. In the Name text box, type a name for the driver.

    I Interacted with the form until it contained this info:
    
    Name: Amazon Redshift
    Library: /home/dan/sqlwb/ext/RedshiftJDBC42-1.2.16.1027.jar
    Classname: com.amazon.redshift.jdbc.Driver
    Sample URL: jdbc:redshift://endpoint:port/database
    
