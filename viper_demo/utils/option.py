from utils.log import logger

option_type_default_length = {
    'float': 6,
    'integer': 6,
    'bool': 6,
    'enum': 6,
    'str': 12,
    'address': 12,
    'address_range': 18,
}


class _Option(object):
    def __init__(
            self,
            name,
            tag_zh=None,
            tag_en=None,
            desc_zh=None,
            desc_en=None,
            type_value="str",
            required=False,
            default=None,
            enum_list=None,
            length=None,
            extra_data=None
    ):
        if enum_list is None:
            enum_list = []

        self._name = name  # 参数名称

        if tag_zh is None:
            self._tag_zh = name
        else:
            self._tag_zh = tag_zh  # 参数的前端显示名称(前端显示用,例如如果name为"path",则name_tag为"路径")

        if desc_zh is None:
            self._desc_zh = name
        else:
            self._desc_zh = desc_zh  # 参数提示信息,详细描述参数作用

        if tag_en is None:
            self._tag_en = name
        else:
            self._tag_en = tag_en  # 参数的前端显示名称(前端显示用,例如如果name为"path",则name_tag为"路径")

        if desc_en is None:
            self._desc_en = name
        else:
            self._desc_en = desc_en  # 参数提示信息,详细描述参数作用

        self._type = type_value  # 参数类型,参考option_type_list
        self._required = required  # 是否必填
        self._default = default  # 参数默认值
        self._enum_list = enum_list  # enum类型的待选列表,如果type为enum类型则此参数必须填写
        self._length = length  # 参数在前端需要的UI长度 1表示24表示最长
        self._extra_data = extra_data  # 参数需要传递的额外信息

    def to_dict(self):
        """将参数对象转化为json格式数据"""
        _dict = {
            'name': self._name,
            'tag_zh': self._tag_zh,
            'desc_zh': self._desc_zh,
            'tag_en': self._tag_en,
            'desc_en': self._desc_en,
            'type': self._type,
            'required': self._required,
            'default': self._default,
            'extra_data': self._extra_data,
        }

        # 处理option_length参数的兼容性
        if self._length is None:
            _dict['length'] = option_type_default_length.get(self._type)
        else:
            _dict['length'] = self._length

        # 处理enum_list参数的兼容性,请注意,此处无法处理handler和凭证等动态参数
        tmp_enmu_list = []
        for one_enmu in self._enum_list:
            if isinstance(one_enmu, str) or isinstance(one_enmu, bytes):
                tmp_enmu_list.append({'name': one_enmu, 'value': one_enmu})
            else:
                if one_enmu.get('tag_zh') is not None and one_enmu.get('value') is not None:
                    tmp_enmu_list.append(one_enmu)
                else:
                    logger.warning(f"参数错误, name: {self._name} tag_zh:{self._tag_zh}")
        _dict['enum_list'] = tmp_enmu_list
        return _dict


class OptionStr(_Option):
    def __init__(self,
                 name,
                 tag_zh=None,
                 tag_en=None,
                 desc_zh=None,
                 desc_en=None,
                 required=False,
                 default=None,
                 length=None
                 ):
        super().__init__(name=name, tag_zh=tag_zh, desc_zh=desc_zh, tag_en=tag_en, desc_en=desc_en,
                         required=required, default=default,
                         length=length)


HANDLER_OPTION = {
    'name': '_msgrpc_handler',

    'tag_zh': '监听',
    'desc_zh': '模块需要的监听器',

    'tag_en': 'Handler',
    'desc_en': 'Handler config that use by module',

    'type': 'enum',
    'option_length': 24
}


class OptionHandler(_Option):
    """监听配置参数"""

    def __init__(self, required=True):
        super().__init__(type_value='enum',
                         name=HANDLER_OPTION.get('name'),
                         tag_zh=HANDLER_OPTION.get('tag_zh'),
                         desc_zh=HANDLER_OPTION.get('desc_zh'),
                         tag_en=HANDLER_OPTION.get('tag_en'),
                         desc_en=HANDLER_OPTION.get('desc_en'),
                         length=HANDLER_OPTION.get('option_length'),
                         required=required,
                         )


def register_options(options_list=None):
    """注册模块参数"""
    if options_list is None:
        options_list = []
    options = []
    try:
        for option in options_list:
            options.append(option.to_dict())
        return options
    except Exception as E:
        logger.error(E)
        return []
