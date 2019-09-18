import axios from "axios"

export const GET_PROVINCE_LIST = "GET_PROVINCE_LIST"
export const FOUND_PROVINCE_LIST = "FOUND_PROVINCE_LIST"
export const NOT_FOUND_PROVINCE = "NOT_FOUND_PROVINCE"

function actionGetProvince(data) {
    return {
        type: data.type,
        results: data.results
    }
}

// get provinces data
export function getProvinceList() {
    return dispatch => {

        dispatch(actionGetProvince({ type: GET_PROVINCE_LIST, results: [] }))

        // request the api server
        axios.get('/api/province/list/').then(response => {

            let provinceList = response.data.results

            // 404 data
            if (provinceList.length == 0) dispatch(actionGetProvince({ type: NOT_FOUND_PROVINCE, results: [] }))
            else dispatch(actionGetProvince({ type: FOUND_PROVINCE_LIST, results: provinceList }))

            // if has an error
        }).catch(err => dispatch(actionGetProvince({ type: NOT_FOUND_PROVINCE, results: [] })))
    }
}
