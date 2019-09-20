import {
    GET_DISTRICT_LIST,
    NOT_FOUND_DISTRICT,
    FOUND_DISTRICT_LIST
} from "../actions/districts"


const initalState = {
    'district_list': [],
    'district_iist_status': false,
    'district_list_isLoading': true,
    // now pagination
    'district_list_pagination': {
        'limit': 0,
        'offset': 0,
        'count': 0,
    }
}


export default function districtReducer(state = initalState, aciton) {

    switch (aciton.type) {

        case GET_DISTRICT_LIST:

            return {
                ...state,
                district_list_isLoading: true
            }

        case FOUND_DISTRICT_LIST:

            return {
                ...state,
                district_list: [...aciton.data],
                district_iist_status: true,
                district_list_isLoading: false,
                district_list_pagination: {
                    ...state.district_list_pagination,
                    limit: aciton.pagination.limit,
                    count: aciton.pagination.count,
                    offset: aciton.pagination.offset
                }
            }

            break;

        case NOT_FOUND_DISTRICT:

            return {
                ...state,
                district_iist_status: false,
                district_list_isLoading: false,
                district_list_pagination: {
                    ...state.district_list_pagination,
                    limit: aciton.pagination.limit,
                    count: aciton.pagination.count,
                    offset: aciton.pagination.offset
                }
            }

            break;
    }



    return state
}