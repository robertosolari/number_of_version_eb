import boto3
def get_total_application_versions():
    # Initialize the Elastic Beanstalk client
    eb_client = boto3.client('elasticbeanstalk')

    # Get all applications
    apps = eb_client.describe_applications()
    total_versions = 0

    # Loop through each application to get the count of its application versions
    for app in apps['Applications']:
        app_name = app['ApplicationName']

        # Paginate through application versions if you have many versions
        paginator = eb_client.get_paginator('describe_application_versions')
        page_iterator = paginator.paginate(ApplicationName=app_name)

        for page in page_iterator:
            total_versions += len(page['ApplicationVersions'])

    return total_versions


if __name__ == "__main__":
    total = get_total_application_versions()
    print(f"Total application versions across all applications: {total}")

