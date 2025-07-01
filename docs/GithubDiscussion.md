# GithubDiscussion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**number** | **int** |  | 
**html_url** | **str** |  | 
**answer_html_url** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**user** | [**GithubUser**](GithubUser.md) |  | 

## Example

```python
from dc_rest.models.github_discussion import GithubDiscussion

# TODO update the JSON string below
json = "{}"
# create an instance of GithubDiscussion from a JSON string
github_discussion_instance = GithubDiscussion.from_json(json)
# print the JSON string representation of the object
print(GithubDiscussion.to_json())

# convert the object into a dict
github_discussion_dict = github_discussion_instance.to_dict()
# create an instance of GithubDiscussion from a dict
github_discussion_from_dict = GithubDiscussion.from_dict(github_discussion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


