import {
    GET_PROVINCE_LIST,
    FOUND_PROVINCE_LIST,
    NOT_FOUND_PROVINCE
} from "../actions/province"


const initialState = {
    'provinces_data': [],
    'status': false,
    'isLoading': true
}

function ProvinceReducer(state = initialState, action) {

    switch (action.type) {

        case NOT_FOUND_PROVINCE:
            return {
                ...state,
                isLoading: false
            }

            break;

        case FOUND_PROVINCE_LIST:
            return {
                ...state,
                provinces_data: [...state.provinces_data, ...action.results],
                isLoading: false,
                status: true
            }

            break;
    }

    return state
}

export default ProvinceReducer