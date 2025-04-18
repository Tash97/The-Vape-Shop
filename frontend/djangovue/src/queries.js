import gql from "graphql-tag";


export const SITE_INFO = gql`
  query {
    allCategories {
      name
    }
  }
`;