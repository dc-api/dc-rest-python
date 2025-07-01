# GithubIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 
**html_url** | **str** |  | 
**user** | [**GithubUser**](GithubUser.md) |  | 
**title** | **str** |  | 
**body** | **str** |  | [optional] 
**pull_request** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.github_issue import GithubIssue

# TODO update the JSON string below
json = "{}"
# create an instance of GithubIssue from a JSON string
github_issue_instance = GithubIssue.from_json(json)
# print the JSON string representation of the object
print(GithubIssue.to_json())

# convert the object into a dict
github_issue_dict = github_issue_instance.to_dict()
# create an instance of GithubIssue from a dict
github_issue_from_dict = GithubIssue.from_dict(github_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


