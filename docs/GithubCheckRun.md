# GithubCheckRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **str** |  | [optional] 
**name** | **str** |  | 
**html_url** | **str** |  | 
**check_suite** | [**GithubCheckSuite**](GithubCheckSuite.md) |  | 
**details_url** | **str** |  | [optional] 
**output** | [**GithubCheckRunOutput**](GithubCheckRunOutput.md) |  | [optional] 
**pull_requests** | [**List[GithubCheckPullRequest]**](GithubCheckPullRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.github_check_run import GithubCheckRun

# TODO update the JSON string below
json = "{}"
# create an instance of GithubCheckRun from a JSON string
github_check_run_instance = GithubCheckRun.from_json(json)
# print the JSON string representation of the object
print(GithubCheckRun.to_json())

# convert the object into a dict
github_check_run_dict = github_check_run_instance.to_dict()
# create an instance of GithubCheckRun from a dict
github_check_run_from_dict = GithubCheckRun.from_dict(github_check_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


