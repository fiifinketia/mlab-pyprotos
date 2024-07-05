# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runner.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0crunner.proto\x12\x06runner\"\x12\n\x10GetRunnerRequest\"#\n\x11GetRunnerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x11\n\x0fStopTaskRequest\"\x12\n\x10StopTaskResponse\"\x13\n\x11RemoveTaskRequest\"\x14\n\x12RemoveTaskResponse\"e\n\x11\x43reateTaskRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12 \n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32\x0f.runner.Project\x12\x1e\n\x05model\x18\x03 \x01(\x0b\x32\x0f.runner.Project\"\x14\n\x12\x43reateTaskResponse\"\x1b\n\x19GetTaskEnvironmentRequest\"\x1c\n\x1aGetTaskEnvironmentResponse\"\xfd\x01\n\x0eRunTaskRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x11\n\ttask_name\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x13\n\x0bresults_dir\x18\x05 \x01(\t\x12\x10\n\x08\x62\x61se_dir\x18\x06 \x01(\t\x12\x0f\n\x07rpc_url\x18\x07 \x01(\t\x12\x1e\n\x05model\x18\x08 \x01(\x0b\x32\x0f.runner.Project\x12 \n\x07\x64\x61taset\x18\t \x01(\x0b\x32\x0f.runner.Project\x12\x1a\n\rtrained_model\x18\n \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_trained_model\"o\n\x07Project\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04path\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04type\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x62ranch\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_pathB\x07\n\x05_typeB\t\n\x07_branch\"S\n\x0fRunTaskResponse\x12\x0e\n\x04line\x18\x01 \x01(\x0cH\x00\x12$\n\x06result\x18\x02 \x01(\x0b\x32\x12.runner.TaskResultH\x00\x42\n\n\x08response\"Q\n\x0c\x42ytesContent\x12\x11\n\tfile_size\x18\x01 \x01(\x03\x12\x0e\n\x06\x62uffer\x18\x02 \x01(\x0c\x12\x1e\n\x04info\x18\x03 \x01(\x0b\x32\x10.runner.FileInfo\"\xba\x01\n\nTaskResult\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12#\n\x05\x66iles\x18\x03 \x03(\x0b\x32\x14.runner.BytesContent\x12 \n\x07metrics\x18\x04 \x03(\x0b\x32\x0f.runner.Metrics\x12\x10\n\x08pkg_name\x18\x05 \x01(\t\x12\x1d\n\x10pretrained_model\x18\x06 \x01(\tH\x00\x88\x01\x01\x42\x13\n\x11_pretrained_model\"+\n\x08\x46ileInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t\"&\n\x07Metrics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x15\n\x13SubmitResultRequest\"\x16\n\x14SubmitResultResponse2\x8d\x04\n\x06Runner\x12\x41\n\nget_runner\x12\x18.runner.GetRunnerRequest\x1a\x19.runner.GetRunnerResponse\x12>\n\tstop_task\x12\x17.runner.StopTaskRequest\x1a\x18.runner.StopTaskResponse\x12\x44\n\x0bremove_task\x12\x19.runner.RemoveTaskRequest\x1a\x1a.runner.RemoveTaskResponse\x12P\n\x17\x63reate_task_environment\x12\x19.runner.CreateTaskRequest\x1a\x1a.runner.CreateTaskResponse\x12]\n\x14get_task_environment\x12!.runner.GetTaskEnvironmentRequest\x1a\".runner.GetTaskEnvironmentResponse\x12=\n\x08run_task\x12\x16.runner.RunTaskRequest\x1a\x17.runner.RunTaskResponse0\x01\x12J\n\rsubmit_result\x12\x1b.runner.SubmitResultRequest\x1a\x1c.runner.SubmitResultResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'runner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETRUNNERREQUEST']._serialized_start=24
  _globals['_GETRUNNERREQUEST']._serialized_end=42
  _globals['_GETRUNNERRESPONSE']._serialized_start=44
  _globals['_GETRUNNERRESPONSE']._serialized_end=79
  _globals['_STOPTASKREQUEST']._serialized_start=81
  _globals['_STOPTASKREQUEST']._serialized_end=98
  _globals['_STOPTASKRESPONSE']._serialized_start=100
  _globals['_STOPTASKRESPONSE']._serialized_end=118
  _globals['_REMOVETASKREQUEST']._serialized_start=120
  _globals['_REMOVETASKREQUEST']._serialized_end=139
  _globals['_REMOVETASKRESPONSE']._serialized_start=141
  _globals['_REMOVETASKRESPONSE']._serialized_end=161
  _globals['_CREATETASKREQUEST']._serialized_start=163
  _globals['_CREATETASKREQUEST']._serialized_end=264
  _globals['_CREATETASKRESPONSE']._serialized_start=266
  _globals['_CREATETASKRESPONSE']._serialized_end=286
  _globals['_GETTASKENVIRONMENTREQUEST']._serialized_start=288
  _globals['_GETTASKENVIRONMENTREQUEST']._serialized_end=315
  _globals['_GETTASKENVIRONMENTRESPONSE']._serialized_start=317
  _globals['_GETTASKENVIRONMENTRESPONSE']._serialized_end=345
  _globals['_RUNTASKREQUEST']._serialized_start=348
  _globals['_RUNTASKREQUEST']._serialized_end=601
  _globals['_PROJECT']._serialized_start=603
  _globals['_PROJECT']._serialized_end=714
  _globals['_RUNTASKRESPONSE']._serialized_start=716
  _globals['_RUNTASKRESPONSE']._serialized_end=799
  _globals['_BYTESCONTENT']._serialized_start=801
  _globals['_BYTESCONTENT']._serialized_end=882
  _globals['_TASKRESULT']._serialized_start=885
  _globals['_TASKRESULT']._serialized_end=1071
  _globals['_FILEINFO']._serialized_start=1073
  _globals['_FILEINFO']._serialized_end=1116
  _globals['_METRICS']._serialized_start=1118
  _globals['_METRICS']._serialized_end=1156
  _globals['_SUBMITRESULTREQUEST']._serialized_start=1158
  _globals['_SUBMITRESULTREQUEST']._serialized_end=1179
  _globals['_SUBMITRESULTRESPONSE']._serialized_start=1181
  _globals['_SUBMITRESULTRESPONSE']._serialized_end=1203
  _globals['_RUNNER']._serialized_start=1206
  _globals['_RUNNER']._serialized_end=1731
# @@protoc_insertion_point(module_scope)
