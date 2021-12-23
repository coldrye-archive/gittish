# Protocol Documentation
<a name="top"/>

## Table of Contents
* [actor.proto](#actor.proto)
 * [Actor](#gittish.protocol.Actor)
 * [Actor.Type](#gittish.protocol.Actor.Type)
* [error.proto](#error.proto)
 * [CommonErrorType](#gittish.protocol.CommonErrorType)
 * [EntityErrorType](#gittish.protocol.EntityErrorType)
 * [Error](#gittish.protocol.Error)
 * [NetworkErrorType](#gittish.protocol.NetworkErrorType)
 * [CommonErrorType.Type](#gittish.protocol.CommonErrorType.Type)
 * [EntityErrorType.Type](#gittish.protocol.EntityErrorType.Type)
 * [NetworkErrorType.Type](#gittish.protocol.NetworkErrorType.Type)
* [name.proto](#name.proto)
 * [Name](#gittish.protocol.Name)
* [id.proto](#id.proto)
 * [Id](#gittish.protocol.Id)
* [operation.proto](#operation.proto)
 * [CommonOperationType](#gittish.protocol.CommonOperationType)
 * [Operation](#gittish.protocol.Operation)
 * [CommonOperationType.Type](#gittish.protocol.CommonOperationType.Type)
* [reqres.proto](#reqres.proto)
 * [Reqres](#gittish.protocol.Reqres)
 * [Reqres.Type](#gittish.protocol.Reqres.Type)
* [timing_info.proto](#timing_info.proto)
 * [TimingInfo](#gittish.protocol.TimingInfo)
* [Scalar Value Types](#scalar-value-types)

<a name="actor.proto"/>
<p align="right"><a href="#top">Top</a></p>

## actor.proto



<a name="gittish.protocol.Actor"/>
### Actor
The message Actor models an actor on whose behalf a given operation is to be
executed.

Actors can be either individuals or organizations, both of which are
represented as actors of type ORGANIZATION.

For internal use only, there is the SYSTEM actor.

And, for anonymous (web) access to the data, there is also the ANONYMOUS
actor.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Actor.Type](#gittish.protocol.Actor.Type) | optional | TBD:DOCUMENT |
| id | [Id](#gittish.protocol.Id) | optional | The id of the actor. For the system/anonymous actor this is left blank. |
| name | [Name](#gittish.protocol.Name) | optional | The name of the actor. For the system/anonymous actor this is left blank. |



<a name="gittish.protocol.Actor.Type"/>
### Actor.Type
TBD:DOCUMENT

| Name | Number | Description |
| ---- | ------ | ----------- |
| SYSTEM | 0 | The SYSTEM actor. |
| ANONYMOUS | 1 | The ANONYMOUS actor. |
| ORGANIZATION | 2 | The ORGANIZATION actor. |




<a name="error.proto"/>
<p align="right"><a href="#top">Top</a></p>

## error.proto



<a name="gittish.protocol.CommonErrorType"/>
### CommonErrorType
TBD:DOCUMENT

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [CommonErrorType.Type](#gittish.protocol.CommonErrorType.Type) | optional |  |


<a name="gittish.protocol.EntityErrorType"/>
### EntityErrorType
TBD:DOCUMENT

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [EntityErrorType.Type](#gittish.protocol.EntityErrorType.Type) | optional |  |


<a name="gittish.protocol.Error"/>
### Error
TBD:DOCUMENT

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Any](#google.protobuf.Any) | optional | TBD:DOCUMENT |
| data | [Any](#google.protobuf.Any) | optional | TBD:DOCUMENT |
| detail | [string](#string) | repeated | TBD:DOCUMENT |


<a name="gittish.protocol.NetworkErrorType"/>
### NetworkErrorType
TBD:DOCUMENT

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [NetworkErrorType.Type](#gittish.protocol.NetworkErrorType.Type) | optional |  |



<a name="gittish.protocol.CommonErrorType.Type"/>
### CommonErrorType.Type
TBD:DOCUMENT

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 | TBD:DOCUMENTAn unspecified and unexpected, non recoverable error. |
| INTERNAL | 1 | TBD:DOCUMENTInternal error occurring, e.g. connection to database backend failure orsimilar such errors. |
| OUT_OF_MEMORY | 2 | TBD:DOCUMENTThe request could not be processed due to memory limitations. |

<a name="gittish.protocol.EntityErrorType.Type"/>
### EntityErrorType.Type
TBD:DOCUMENT

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNAVAIL | 0 | TBD:DOCUMENTAn entity by that name/id is not available. |
| EXISTS | 1 | TBD:DOCUMENTAn entity by that name/id already exists. |
| MISMATCH | 2 | TBD:DOCUMENTAn update to an entity failed due to a version mismatch. |
| INVALID | 3 | TBD:DOCUMENTThe provided data failed validation. |

<a name="gittish.protocol.NetworkErrorType.Type"/>
### NetworkErrorType.Type
TBD:DOCUMENT

| Name | Number | Description |
| ---- | ------ | ----------- |
| ILLEGAL_REQUEST | 0 | TBD:DOCUMENTThe request being made is illegal in the given client/service context. |
| INVALID_REQUEST | 1 | TBD:DOCUMENTThe request could not be validated. |
| HUNG_UP | 2 | TBD:DOCUMENTThe connected client or service hung up prematurely. |
| TIMEOUT | 3 | TBD:DOCUMENTThere was a timeout waiting for additional requests/responses from theconnected client or service. |




<a name="name.proto"/>
<p align="right"><a href="#top">Top</a></p>

## name.proto



<a name="gittish.protocol.Name"/>
### Name
The message Name models a name of some sort, for example the name of an
actor or a repository.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) | optional | The name's value, a string. There exist certain restrictions on a name'svalue dependening on the context in which it is being used. |






<a name="id.proto"/>
<p align="right"><a href="#top">Top</a></p>

## id.proto



<a name="gittish.protocol.Id"/>
### Id
The message Id models an id of some sort, for example the id of an
actor or a repository.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [bytes](#bytes) | optional | The id's value, a byte array. There exist certain restrictions on an id'svalue dependening on the context in which it is being used. |






<a name="operation.proto"/>
<p align="right"><a href="#top">Top</a></p>

## operation.proto



<a name="gittish.protocol.CommonOperationType"/>
### CommonOperationType
Common Operation Types

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [CommonOperationType](#gittish.protocol.CommonOperationType) | optional | TBD:DOCUMENT |


<a name="gittish.protocol.Operation"/>
### Operation
TBD:DOCUMENT

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Any](#google.protobuf.Any) | optional | The operation target's specific operation type or a common operation type. |
| data | [Any](#google.protobuf.Any) | optional | Operation specific data. |



<a name="gittish.protocol.CommonOperationType.Type"/>
### CommonOperationType.Type
TBD:DOCUMENT

| Name | Number | Description |
| ---- | ------ | ----------- |
| CREATE | 0 | TBD:DOCUMENT |
| DELETE | 1 | TBD:DOCUMENT |
| RENAME | 2 | TBD:DOCUMENT |
| UPDATE | 3 | TBD:DOCUMENT |
| LOOKUP | 4 | TBD:DOCUMENT |
| BROWSE | 5 | TBD:DOCUMENT |




<a name="reqres.proto"/>
<p align="right"><a href="#top">Top</a></p>

## reqres.proto



<a name="gittish.protocol.Reqres"/>
### Reqres
The message Reqres models a unified approach to request/response messaging.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Reqres.Type](#gittish.protocol.Reqres.Type) | optional | The type of the request/response. |
| actor | [Actor](#gittish.protocol.Actor) | optional | Request only. The actor on whose behalf a request is being made. |
| timing | [TimingInfo](#gittish.protocol.TimingInfo) | optional | Response only. Optional timing info on how long it took to process therequest. |
| data | [Any](#google.protobuf.Any) | optional | Optional request/response specific data. |



<a name="gittish.protocol.Reqres.Type"/>
### Reqres.Type
The request/response type.

| Name | Number | Description |
| ---- | ------ | ----------- |
| REQUEST | 0 | A standard (operation) request. |
| RESPONSE | 1 | A standard (operation) response. |
| ERROR | 2 | Indicates an unrecoverable error either in form of a streaming requestor a (streaming) response. |
| STREAM | 3 | Indicates a stream request/response which involves multiple data segmentsto be send over the wire.See gittish-core-protocol-streaming for more details. |
| ACK | 4 | Indicates an ACK response to a (streaming) request/response.Not all internal protocols require acknowledgment of individual streamrequests/responses.While an ACK normally does not require any data, certain services a/oclients might provide optional data, for example the push service orthe pull client. |
| FIN | 5 | Indicates the end of a sequence of (streaming) requests/responses. |




<a name="timing_info.proto"/>
<p align="right"><a href="#top">Top</a></p>

## timing_info.proto



<a name="gittish.protocol.TimingInfo"/>
### TimingInfo
The message TimingInfo is included with every service response.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| begin | [uint64](#uint64) | optional | The time in milliseconds the operation was begun. |
| end | [uint64](#uint64) | optional | The time in milliseconds the operation ended. |







<a name="scalar-value-types"/>
## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double"/> double |  | double | double | float |
| <a name="float"/> float |  | float | float | float |
| <a name="int32"/> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64"/> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32"/> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64"/> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32"/> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64"/> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32"/> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64"/> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32"/> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64"/> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool"/> bool |  | bool | boolean | boolean |
| <a name="string"/> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes"/> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |
