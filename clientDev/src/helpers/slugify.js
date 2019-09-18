

export default function slugify(Text) {
    return Text.toLowerCase().replace(/\s/g, '-').replace(/[^\w-/]+/g, '')

}