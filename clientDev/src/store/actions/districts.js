export const GET_DISTRICT_LIST = "GET_DISTRICT_LIST"
export const FOUND_DISTRICT_LIST = "FOUND_DISTRICT_LIST"
export const NOT_FOUND_DISTRICT = "NOT_FOUND_DISTRICT"


export function get_districtList(limit, offset) {

    return dispatch => {

        // request endpoint
        dispatch({ type: GET_DISTRICT_LIST })

        const END_POINT = `/api/district/list/?limit=${limit}&offset=${offset}`

        fetch(END_POINT).then(res => {

            if (res.ok) return res.json()
            else Promise.reject(res.statusText)

        }).then(data => {
            // success

            // no data 
            if (data.count == 0) {

                dispatch({
                    type: NOT_FOUND_DISTRICT,
                    status: false,
                    loading: false,
                    pagination: {
                        limit: 0,
                        count: 0,
                        offset: 0
                    }
                })

                // has data
            } else {
                dispatch({
                    type: FOUND_DISTRICT_LIST,
                    status: true,
                    data: data.results,
                    loading: true,
                    pagination: {
                        limit: limit,
                        count: data.count,
                        offset: offset
                    }
                })
            }

        }).catch(err => {

            // error
            dispatch({
                type: NOT_FOUND_DISTRICT,
                status: false,
                loading: false,
                pagination: {
                    limit: 0,
                    count: 0,
                    offset: 0
                }
            })
        })
    }
}