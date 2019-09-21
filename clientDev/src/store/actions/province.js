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

        fetch('/api/province/list/').then(res => {
            if (res.ok) return res.json()
            else Promise.reject(res.status)
        }).then(data => {
            // success

            // han't data
            if (data.count == 0) dispatch(actionGetProvince({ type: NOT_FOUND_PROVINCE, results: [] }))
            else dispatch(actionGetProvince({ type: FOUND_PROVINCE_LIST, results: data.results }))


        }).catch(err => {
            //err
            dispatch(actionGetProvince({ type: NOT_FOUND_PROVINCE, results: [] }))
        })
    }
}
