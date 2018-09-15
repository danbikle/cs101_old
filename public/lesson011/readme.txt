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

