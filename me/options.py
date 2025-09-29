import rendercv.themes.options
import pydantic


class MEducationEntryBase(RenderCVBaseModelWithoutExtraKeys):
    """Base options for education entries."""

    main_column_first_row_template: str = (
        education_entry_main_column_first_row_template_field_info
    )
    degree_column_template: Optional[str] = (
        education_entry_degree_column_template_field_info
    )
    degree_column_width: TypstDimension = education_entry_degree_column_width_field_info


class MEducationEntryOptions(EntryBaseWithDate, MEducationEntryBase):
    """Options related to education entries."""

    model_config = pydantic.ConfigDict(title="Modified Education Entry Options")
