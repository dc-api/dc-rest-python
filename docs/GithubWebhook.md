# GithubWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**ref_type** | **str** |  | [optional] 
**comment** | [**GithubComment**](GithubComment.md) |  | [optional] 
**issue** | [**GithubIssue**](GithubIssue.md) |  | [optional] 
**pull_request** | [**GithubIssue**](GithubIssue.md) |  | [optional] 
**repository** | [**GithubRepository**](GithubRepository.md) |  | [optional] 
**forkee** | [**GithubRepository**](GithubRepository.md) |  | [optional] 
**sender** | [**GithubUser**](GithubUser.md) |  | 
**member** | [**GithubUser**](GithubUser.md) |  | [optional] 
**release** | [**GithubRelease**](GithubRelease.md) |  | [optional] 
**head_commit** | [**GithubCommit**](GithubCommit.md) |  | [optional] 
**commits** | [**List[GithubCommit]**](GithubCommit.md) |  | [optional] 
**forced** | **bool** |  | [optional] 
**compare** | **str** |  | [optional] 
**review** | [**GithubReview**](GithubReview.md) |  | [optional] 
**check_run** | [**GithubCheckRun**](GithubCheckRun.md) |  | [optional] 
**check_suite** | [**GithubCheckSuite**](GithubCheckSuite.md) |  | [optional] 
**discussion** | [**GithubDiscussion**](GithubDiscussion.md) |  | [optional] 
**answer** | [**GithubComment**](GithubComment.md) |  | [optional] 

## Example

```python
from dc_rest.models.github_webhook import GithubWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of GithubWebhook from a JSON string
github_webhook_instance = GithubWebhook.from_json(json)
# print the JSON string representation of the object
print(GithubWebhook.to_json())

# convert the object into a dict
github_webhook_dict = github_webhook_instance.to_dict()
# create an instance of GithubWebhook from a dict
github_webhook_from_dict = GithubWebhook.from_dict(github_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


