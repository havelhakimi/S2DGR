# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

__all__ = []

# 使用try-except来处理可能缺失的模块
try:
    from genrec.models.S2DGR.model import S2DGR
except ImportError:
    S2DGR = None
    print("Warning: S2DGR model not found, skipping import")

try:
    from genrec.models.AR_GRM.model import AR_GRM
except ImportError:
    AR_GRM = None
    print("Warning: AR_GRM model not found, skipping import")


# 只导出存在的模型
if S2DGR is not None:
    __all__.append('S2DGR')
if AR_GRM is not None:
    __all__.append('AR_GRM')

