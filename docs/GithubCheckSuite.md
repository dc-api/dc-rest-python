# GithubCheckSuite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **str** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_sha** | **str** |  | 
**pull_requests** | [**List[GithubCheckPullRequest]**](GithubCheckPullRequest.md) |  | [optional] 
**app** | [**GithubCheckApp**](GithubCheckApp.md) |  | 

## Example

```python
from dc_rest.models.github_check_suite import GithubCheckSuite

# TODO update the JSON string below
json = "{}"
# create an instance of GithubCheckSuite from a JSON string
github_check_suite_instance = GithubCheckSuite.from_json(json)
# print the JSON string representation of the object
print(GithubCheckSuite.to_json())

# convert the object into a dict
github_check_suite_dict = github_check_suite_instance.to_dict()
# create an instance of GithubCheckSuite from a dict
github_check_suite_from_dict = GithubCheckSuite.from_dict(github_check_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


